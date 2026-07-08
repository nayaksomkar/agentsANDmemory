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

## Config (`config.json`)

```json
{
  "model": "gemini-2.5-flash",
  "temperature": 0.7,
  "SamplesQueries": [
    "What is 125 * 45 + 78 / 3 ?",
    "Can you count the words in I am learning LangChain and LangGraph today please",
    "Please tell me how many characters are in LangChain Framework",
    "Calculate ((25 + 75) * 4) / 2"
  ]
}
```

---

## Run

```bash
uv run python main.py
```

---

## Output

The agent prints the full conversation history after each query. Sample run:

```text
[
    {"role": "user", "content": "What is 125 * 45 + 78 / 3 ?"},
    {"role": "assistant", "content": "The result is **5,651**."}
]
[
    {"role": "user", "content": "What is 125 * 45 + 78 / 3 ?"},
    {"role": "assistant", "content": "The result is **5,651**."},
    {"role": "user", "content": "Can you count the words in I am learning LangChain and LangGraph today please"},
    {"role": "assistant", "content": "The sentence contains **7 words**."}
]
[
    {"role": "user", "content": "What is 125 * 45 + 78 / 3 ?"},
    {"role": "assistant", "content": "The result is **5,651**."},
    {"role": "user", "content": "Can you count the words in I am learning LangChain and LangGraph today please"},
    {"role": "assistant", "content": "The sentence contains **7 words**."},
    {"role": "user", "content": "Please tell me how many characters are in LangChain Framework"},
    {"role": "assistant", "content": "The phrase **\"LangChain Framework\"** contains **18 characters** (including the space)."}
]
[
    {"role": "user", "content": "What is 125 * 45 + 78 / 3 ?"},
    {"role": "assistant", "content": "The result is **5,651**."},
    {"role": "user", "content": "Can you count the words in I am learning LangChain and LangGraph today please"},
    {"role": "assistant", "content": "The sentence contains **7 words**."},
    {"role": "user", "content": "Please tell me how many characters are in LangChain Framework"},
    {"role": "assistant", "content": "The phrase **\"LangChain Framework\"** contains **18 characters** (including the space)."},
    {"role": "user", "content": "Calculate ((25 + 75) * 4) / 2"},
    {"role": "assistant", "content": "The result is **200**."}
]
```
