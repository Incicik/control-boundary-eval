"""
Control-Boundary Eval: OpenAI Client Adapter
Handles authenticated API transport to official OpenAI GPT models.
"""

import os
from openai import OpenAI
from src.models.base import BaseModelAdapter

class OpenAIAdapter(BaseModelAdapter):
    """
    Adapter for interacting with OpenAI's Chat Completions API.
    """
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.model_name = model_name

    def generate_response(self, prompt: str, system_prompt: str = "") -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        try:
            completion = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                max_tokens=1024
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"API transport error: {str(e)}"

    def run_multi_step_conversation(self, prompts: list[str], system_prompt: str = "") -> list[str]:
        responses = []
        conversation_history = []
        
        if system_prompt:
            conversation_history.append({"role": "system", "content": system_prompt})

        for prompt in prompts:
            conversation_history.append({"role": "user", "content": prompt})
            try:
                completion = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=conversation_history,
                    max_tokens=1024
                )
                model_output = completion.choices[0].message.content
                responses.append(model_output)
                conversation_history.append({"role": "assistant", "content": model_output})
            except Exception as e:
                error_msg = f"API multi-turn transport error: {str(e)}"
                responses.append(error_msg)
                break
                
        return responses
