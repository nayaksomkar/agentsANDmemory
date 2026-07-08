"""Tools for agenttwo. Each is a function wrapped with @tool; its name,
type hints, and docstring describe it to the agent."""
from langchain_core.tools import tool

from datetime import datetime, date


@tool
def temperature_converter(celsius: float) -> str:
    """Converts a Celsius temperature to Fahrenheit and Kelvin."""
    f = celsius * 9 / 5 + 32
    k = celsius + 273.15
    return f"{celsius}°C = {f:.2f}°F = {k:.2f}K"


@tool
def palindrome_checker(text: str) -> str:
    """Checks whether the given text reads the same forwards and backwards."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return f"'{text}' is a palindrome: {cleaned == cleaned[::-1]}"


@tool
def days_until(target_date: str) -> str:
    """Returns the number of days from today until the given date (YYYY-MM-DD)."""
    try:
        d = datetime.strptime(target_date, "%Y-%m-%d").date()
    except Exception as error:
        return f"Error: {error}"
    delta = (d - date.today()).days
    return f"{delta} days until {target_date}"


@tool
def roll_dice(sides: int) -> str:
    """Rolls a die with the given number of sides and returns the result."""
    import random
    return f"Rolled a {sides}-sided die: {random.randint(1, sides)}"
