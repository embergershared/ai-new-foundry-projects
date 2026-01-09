# Microsoft Foundry Quickstart

## Source

[Microsoft Foundry Quickstart](https://learn.microsoft.com/en-us/azure/ai-foundry/quickstarts/get-started-code?view=foundry&tabs=python)

## Steps

```pwsh
# We use uv for the virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

# Check the right Virtual Environment is active
$env:VIRTUAL_ENV

# Recommended structure
my_project/
├── .venv/
├── .env
├── .gitignore
├── pyproject.toml
├── src/
│   ├── __init__.py
│   └── main.py
├── scripts/
├── tests/

uv venv
uv pip install -r requirements.txt
uv run python src/main.py


```
