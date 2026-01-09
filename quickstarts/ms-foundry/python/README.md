# Microsoft Foundry Quickstart

## Source

[Microsoft Foundry Quickstart](https://learn.microsoft.com/en-us/azure/ai-foundry/quickstarts/get-started-code?view=foundry&tabs=python)

## Setup

### Environment Configuration

This project uses two environment files:

- `.env.local` - Template file (checked into git) with placeholder values
- `.env` - Actual file (NOT checked into git) with your sensitive values

**First-time setup:**

1. Copy `.env.local` to `.env`
2. Edit `.env` and set `FOUNDRY_NAME` to your Azure resource name
3. The `.env` file contains your actual values and is excluded from git via `.gitignore`

The `.env` file should contain:

```env
FOUNDRY_NAME="your-actual-resource-name"
```

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
