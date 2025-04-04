# coding_agent.py
from smolagents import CodeAgent, HfApiModel
from coding_tools import code_suggester, code_debugger, docstring_generator, code_formatter

model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct", token="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")

coding_agent = CodeAgent(
    tools=[code_suggester, code_debugger, docstring_generator, code_formatter],
    model=model,
    add_base_tools=True
)
