# coding_agent.py
from smolagents import CodeAgent, TransformersModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

def create_coding_agent():
    # Configuration
    cache_base = os.path.expanduser("~/huggingface_cache")
    os.makedirs(cache_base, exist_ok=True)
    model_name = "Qwen/Qwen2.5-Coder-7B-Instruct"  # Smaller model for testing

    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            trust_remote_code=True,
            torch_dtype="auto"
        )
        return CodeAgent(
            model=TransformersModel(model=model, tokenizer=tokenizer),
            tools=[code_suggester, code_debugger, docstring_generator, code_formatter],
            add_base_tools=True
        )
    except Exception as e:
        print(f"Failed to initialize agent: {str(e)}")
        return None  # Handle gracefully

coding_agent = create_coding_agent()

