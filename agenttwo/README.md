# agenttwo

> A second LangChain agent, independent of `agentONE` — its own tools, config,
> and `messages.json` memory. The agent chooses tools itself; no manual routing.

---

## Tools

| Tool | What it does |
| --- | --- |
| `temperature_converter` | Celsius → Fahrenheit + Kelvin. |
| `palindrome_checker` | Checks if text reads the same backwards. |
| `days_until` | Days from today until a `YYYY-MM-DD` date. |
| `roll_dice` | Rolls an N-sided die. |

---

## Files

| File | Purpose |
| --- | --- |
| `main.py` | Builds the agent, runs `config.json` queries, persists memory. |
| `tool.py` | The four tools, defined with `@tool`. |
| `config.py` | Agent system prompt. |
| `config.json` | `model`, `temperature`, `SamplesQueries`. |
| `messages.json` | Conversation memory. |

---

## Configuration — `config.json`

```json
{
  "model": "openai/gpt-oss-20b",
  "temperature": 0.5,
  "SamplesQueries": [
    "What is 100 degrees Celsius in Fahrenheit and Kelvin?",
    "Is the word A man a plan a canal Panama a palindrome?",
    "How many days until 2026-12-25?",
    "Roll a 20-sided die for me."
  ]
}
```

---

## Sample output

```text
[
  {
    "role": "user",
    "content": "What is 100 degrees Celsius in Fahrenheit and Kelvin?"
  },
  {
    "role": "assistant",
    "content": "100°C is 212.00°F, which is 373.15K."
  },
  {
    "role": "user",
    "content": "Is the word A man a plan a canal Panama a palindrome?"
  },
  {
    "role": "assistant",
    "content": "Yes — ignoring spaces and punctuation, it reads the same backwards."
  },
  {
    "role": "user",
    "content": "How many days until 2026-12-25?"
  },
  {
    "role": "assistant",
    "content": "There are 170 days until 2026-12-25."
  },
  {
    "role": "user",
    "content": "Roll a 20-sided die for me."
  },
  {
    "role": "assistant",
    "content": "You rolled a 20-sided die and got a 5."
  }
]
```

---

## Run

```bash
uv run python agenttwo/main.py
```
