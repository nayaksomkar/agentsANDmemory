# agentsANDmemory

> Agent + memory demos built with **LangChain**. Each agent picks its own tools
> — no manual routing — and persists its conversation history as memory between runs.

---

## Repository layout

| Path | Description |
| --- | --- |
| `main.py` | Runs the `agentONE` demo. |
| `agentONE/` | LangChain agent with calculator / word-count / character-count tools. |
| `agenttwo/` | Independent LangChain agent with converter / palindrome / date / dice tools. |
| `.env.example` | API key template. |

---

## Getting started

```bash
uv sync
cp .env.example .env   # add your NVIDIA_API_KEY
uv run python main.py
```
