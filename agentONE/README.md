# agentONE

> A LangChain agent (`calculator` / `word_counter` / `character_counter`) that
> keeps `messages.json` as memory between runs. The agent chooses tools itself —
> no manual routing.

---

## Files

| File | Purpose |
| --- | --- |
| `main.py` | Builds the agent, runs `config.json` queries, persists memory. |
| `tool.py` | The three tools, defined with `@tool`. |
| `config.py` | Agent system prompt. |
| `config.json` | `model`, `temperature`, `SamplesQueries`. |
| `messages.json` | Conversation memory. |

---

## Run

```bash
uv run python main.py
```
