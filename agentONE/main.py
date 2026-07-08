"""agentONE/main.py — LangChain agent with messages.json as memory."""
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.agents import create_agent as create

import json
import os

from dotenv import load_dotenv

from tool import calculator, word_counter, character_counter
from config import prompt_main

HERE = os.path.dirname(__file__)


def load_config() -> dict:
    with open(os.path.join(HERE, "config.json"), "r") as f:
        return json.load(f)


def load_memory() -> list:
    path = os.path.join(HERE, "messages.json")
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_memory(history: list) -> None:
    with open(os.path.join(HERE, "messages.json"), "w") as f:
        json.dump(history, f, indent=4)


def main() -> None:
    load_dotenv()
    api_key = os.getenv("NVIDIA_API_KEY")
    if not api_key:
        raise RuntimeError("NVIDIA_API_KEY is not set. Copy .env.example to .env and add your key.")

    config = load_config()

    from langchain_nvidia_ai_endpoints import ChatNVIDIA

    llm = ChatNVIDIA(
        model="openai/gpt-oss-20b",
        api_key=api_key,
        temperature=config["temperature"],
        top_p=1,
    )

    tools = [calculator, word_counter, character_counter]
    agent = create(llm, tools=tools, system_prompt=SystemMessage(content=prompt_main))

    history = load_memory()

    for query in config["SamplesQueries"]:
        response = agent.invoke({"messages": [("user", query)]})
        ai_response = response["messages"][-1].content

        history.append({"role": "user", "content": query})
        history.append({"role": "assistant", "content": ai_response})
        save_memory(history)

        print(history)


if __name__ == "__main__":
    main()
