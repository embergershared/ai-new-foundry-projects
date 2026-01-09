# Microsoft Foundry Quickstart

## Source Links

[python source](https://learn.microsoft.com/en-us/azure/ai-foundry/quickstarts/get-started-code?view=foundry&tabs=python)

[C# source](https://learn.microsoft.com/en-us/azure/ai-foundry/quickstarts/get-started-code?view=foundry&tabs=csharp)

## Summary

This quickstart shows how to call a model deployed in a Microsoft Foundry project:

- Authenticates with Azure using `DefaultAzureCredential`.
- Creates an `AIProjectClient` using your Foundry project endpoint.
- Gets an OpenAI-compatible client from the project (`get_openai_client`).
- Sends a chat-completions request (system + user messages) to a deployed model (example uses `gpt-4o`).
- Prints the model’s response text.
