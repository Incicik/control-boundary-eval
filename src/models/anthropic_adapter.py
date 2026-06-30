"""
Control-Boundary Eval: Anthropic Client Adapter
Handles authenticated API transport to official Anthropic Claude models.
"""

import os
from anthropic import Anthropic
from src.models.base import BaseModelAdapter

class AnthropicAdapter(BaseModelAdapter):
    """
    Adapter for interacting with Anthropic's Messages API.
    """
    def __init__(self, model_name: str = "claude-3-5-sonnet-latest"):
        # Expects ANTHROPIC_API_KEY to be set in your shell environment variables
        self.client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        self.model_name = model_name

    def generate_response(self, prompt: str, system_prompt: str = "") -> str:
        try:
            message = self.client.messages.create(
                model=self.model_name,
                max_tokens=1024,
                system=system_prompt if system_prompt else None,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except Exception as e:
            return f"API transport error: {str(e)}"

    def run_multi_step_conversation(self, prompts: list[str], system_prompt: str = "") -> list[str]:
        responses = []
        conversation_history = []
        
        for prompt in prompts:
            conversation_history.append({"role": "user", "content": prompt})
            try:
                message = self.client.messages.create(
                    model=self.model_name,
                    max_tokens=1024,
                    system=system_prompt if system_prompt else None,
                    messages=conversation_history
                )
                model_output = message.content[0].text
                responses.append(model_output)
                # Append the model's response to keep context for the next turn
                conversation_history.append({"role": "assistant", "content": model_output})
            except Exception as e:
                error_msg = f"API multi-turn transport error: {str(e)}"
                responses.append(error_msg)
                break
                
        return responses
