# src/chat-w-model.py
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()
load_dotenv(".env.local", override=True)

# Load environment variables
FOUNDRY_PROJECT_ENDPOINT = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
FOUNDRY_OPENAI_ENDPOINT = os.environ["FOUNDRY_OPENAI_ENDPOINT"]
FOUNDRY_OPENAI_API_VERSION = os.environ["FOUNDRY_OPENAI_API_VERSION"]
MODEL_DEPLOYMENT_NAME = os.environ["MODEL_DEPLOYMENT_NAME"]

print(f"Using FOUNDRY_PROJECT_ENDPOINT: {FOUNDRY_PROJECT_ENDPOINT}")
print(f"Using FOUNDRY_OPENAI_ENDPOINT : {FOUNDRY_OPENAI_ENDPOINT}")
print(f"Using MODEL_DEPLOYMENT_NAME: {MODEL_DEPLOYMENT_NAME}")
print(f"Using FOUNDRY_OPENAI_API_VERSION: {FOUNDRY_OPENAI_API_VERSION}")
print("")

# Using Foundry Project Endpoint
foundry_project_aiprojectclient = AIProjectClient(
    endpoint=FOUNDRY_PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)
foundry_project_openai_client = foundry_project_aiprojectclient.get_openai_client(
    api_version=FOUNDRY_OPENAI_API_VERSION
)
response_1 = foundry_project_openai_client.chat.completions.create(
    model=MODEL_DEPLOYMENT_NAME,
    messages=[
        {"role": "user", "content": "What is the size of France in square kilometers?"}
    ],
)
print(
    f"Foundry Project endpoint response output: \n\t{response_1.choices[0].message.content}"
)
print("")

# Using Foundry OpenAI Endpoint
foundry_openai_aiprojectclient = AIProjectClient(
    endpoint=FOUNDRY_OPENAI_ENDPOINT,
    credential=DefaultAzureCredential(),
)
foundry_openai_openai_client = foundry_openai_aiprojectclient.get_openai_client(
    api_version=FOUNDRY_OPENAI_API_VERSION
)
response_2 = foundry_openai_openai_client.chat.completions.create(
    model=MODEL_DEPLOYMENT_NAME,
    messages=[
        {"role": "user", "content": "What is the size of France in square kilometers?"}
    ],
)
print(
    f"Foundry OpenAI endpoint response output: \n\t{response_2.choices[0].message.content}"
)
