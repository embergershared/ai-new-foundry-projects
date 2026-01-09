import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

# Get environment variables
load_dotenv()
load_dotenv(".env.local", override=True)

api_endpoint = os.getenv("FOUNDRY_OPENAI_ENDPOINT")
api_deployment = os.getenv("FOUNDRY_DEPLOYMENT_NAME")

# Validate mandatory environment variables
if not api_endpoint:
    raise ValueError("FOUNDRY_OPENAI_ENDPOINT environment variable is not set.")
if not api_deployment:
    raise ValueError("FOUNDRY_DEPLOYMENT_NAME environment variable is not set.")

# Authentication using OpenAI SDK + Entra ID (requires az login to be done beforehand)
bearer_token = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

# Creating OpenAI client
openai_client = OpenAI(base_url=api_endpoint, api_key=bearer_token)

# Send a chat completion request
response = openai_client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of the USA?",
        },
    ],
    max_completion_tokens=16384,
    model=api_deployment,
)

# Print the response
print(response.choices[0].message.content)
