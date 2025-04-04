# coding_tools.py
from smolagents import tool
from typing import Optional
import black
import pylint.lint

@tool
def code_suggester(code: str, problem: str) -> str:
    """
    Provides real-time code suggestions given existing code and a problem description.

    Args:
        code (str): The existing code that needs improvement.
        problem (str): A description of the problem or issue with the code.

    Returns:
        str: A suggested improvement or solution for the given problem.
    """
    return f"Suggested improvement for {problem}:\n# Consider using list comprehensions here"


@tool
def code_debugger(error_message: str, code_snippet: str) -> str:
    """
    Analyzes error messages and suggests fixes for a given code snippet.

    Args:
        error_message (str): The error message encountered while running the code.
        code_snippet (str): The code snippet that needs debugging.

    Returns:
        str: Debugging suggestions based on the error message and analysis of the code snippet.
    """
    pylint_results = pylint.lint.Run([code_snippet], do_exit=False)
    return f"Debugging suggestions:\n{pylint_results.linter.stats['by_msg']}"


@tool
def docstring_generator(code: str) -> str:
    """
    Generates Google-style docstrings for Python functions based on the provided code.

    Args:
        code (str): The Python function or module for which a docstring needs to be generated.

    Returns:
        str: A Google-style docstring template for the given code.
    """
    return "Generated docstring:\n\"\"\"Example function\nArgs:\n    param: Example parameter\nReturns:\n    Example return value\"\"\""


@tool
def code_formatter(code: str) -> str:
    """
    Formats Python code using the Black formatter to ensure consistent style.

    Args:
        code (str): The Python code that needs formatting.

    Returns:
        str: The formatted Python code as per Black's style guidelines.
    """
    return black.format_str(code, mode=black.FileMode())
