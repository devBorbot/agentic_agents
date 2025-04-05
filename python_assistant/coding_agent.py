# coding_agent.py
from smolagents import CodeAgent, LocalModel
from transformers import AutoModelForCausalLM, AutoTokenizer
from coding_tools import code_suggester, code_debugger, docstring_generator, code_formatter

# Load the model and tokenizer locally
model_name = "Qwen/Qwen2.5-Coder-32B-Instruct"

# Initialize tokenizer and model for local inference
tokenizer = AutoTokenizer.from_pretrained(model_name)
local_model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")  # Use GPU if available

# Define a wrapper for local inference
class LocalModelWrapper(LocalModel):
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    def generate(self, prompt: str, max_tokens: int = 100):
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")  # Move tensors to GPU if available
        outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

# Create an instance of the local model wrapper
local_model_wrapper = LocalModelWrapper(local_model, tokenizer)

# Initialize the CodeAgent with local inference
coding_agent = CodeAgent(
    tools=[code_suggester, code_debugger, docstring_generator, code_formatter],
    model=local_model_wrapper,
    add_base_tools=True
)

# Example usage of the coding agent
prompt = "Write a Python function to calculate factorial."
response = coding_agent.run(prompt)
print(response)


# # coding_agent.py
# from smolagents import CodeAgent, HfApiModel
# from coding_tools import code_suggester, code_debugger, docstring_generator, code_formatter

# model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct", token="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")

# coding_agent = CodeAgent(
#     tools=[code_suggester, code_debugger, docstring_generator, code_formatter],
#     model=model,
#     add_base_tools=True
# )
