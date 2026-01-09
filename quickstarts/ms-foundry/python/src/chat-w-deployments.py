# src/chat-w-deepseek.py
import os
from dotenv import load_dotenv

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()
load_dotenv(".env.local", override=True)

endpoint = os.getenv("AZURE_EXISTING_AIPROJECT_ENDPOINT")

# List of deployment names to test
deployment_names = [
    "gpt-5.2",
    "gpt-5.2-chat",
    "gpt-5-pro",
    "DeepSeek-V3.2",
    "grok-4",
    "Mistral-Large-3",
]

# The message to send to all models
user_message = "What is the capital of Germany?"

# Temperature setting
temperature = 0.1

# Authentication using OpenAI SDK + Entra ID
bearer_token = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

openai_client = OpenAI(base_url=endpoint, api_key=bearer_token)

print(f"Using endpoint: {endpoint}")
print(f"Testing deployments: {', '.join(deployment_names)}")
print(f"Temperature: {temperature}")
print(f"Question: {user_message}")
print("=" * 60)

# Define column width for deployment names based on longest name
col_width = max(len(name) for name in deployment_names)

for deployment_name in deployment_names:
    try:
        # Try with custom temperature first
        used_default_temp = False
        try:
            completion = openai_client.chat.completions.create(
                model=deployment_name,
                messages=[
                    {
                        "role": "user",
                        "content": user_message,
                    }
                ],
                temperature=temperature,
            )
        except Exception as temp_error:
            # If temperature fails, retry without temperature parameter (use default)
            if (
                "temperature" in str(temp_error).lower()
                and "unsupported" in str(temp_error).lower()
            ):
                completion = openai_client.chat.completions.create(
                    model=deployment_name,
                    messages=[
                        {
                            "role": "user",
                            "content": user_message,
                        }
                    ],
                )
                used_default_temp = True
            else:
                raise temp_error

        response_content = completion.choices[0].message.content
        temp_note = " - switched to default temperature." if used_default_temp else ""
        print(f"{deployment_name:<{col_width}}: {response_content}{temp_note}")
    except Exception as e:
        error_msg = str(e)
        # Simplify common error messages
        if "does not work with the specified model" in error_msg:
            print(
                f"{deployment_name:<{col_width}}: Error - Model does not support chat completions"
            )
        elif "404" in error_msg and "Resource not found" in error_msg:
            print(f"{deployment_name:<{col_width}}: Error - Model deployment not found")
        else:
            print(f"{deployment_name:<{col_width}}: Error - {error_msg}")
