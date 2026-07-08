"""Tools for the agent. Each is a function wrapped with @tool; its name,
type hints, and docstring describe it to the agent."""
from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """Performs maths operations. Input must be a valid math expression."""
    # eval() runs arbitrary Python — fine locally, never on untrusted input.
    try:
        return str(eval(expression))
    except Exception as error:
        return f"Error: {error}"


@tool
def word_counter(text: str) -> str:
    """Counts how many words are in the given text."""
    return f"Word Count: {len(text.split())}"


@tool
def character_counter(text: str) -> str:
    """Counts how many characters are in the given text."""
    return f"Character Count: {len(text)}"
