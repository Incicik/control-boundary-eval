"""
Control-Boundary Eval: Base Model Adapter
Defines the abstract interface that all specific provider adapters must implement.
"""

from abc import ABC, abstractmethod

class BaseModelAdapter(ABC):
    """
    Abstract Base Class for model API interaction.
    Enforces a uniform interface for running multi-turn security experiments.
    """

    @abstractmethod
    def generate_response(self, prompt: str, system_prompt: str = "") -> str:
        """
        Sends a single prompt string to the model and returns the text response.
        Used primarily for evaluating direct baseline requests.
        """
        pass

    @abstractmethod
    def run_multi_step_conversation(self, prompts: list[str], system_prompt: str = "") -> list[str]:
        """
        Executes an isolated multi-turn interaction string sequence.
        Maintains conversational context across the list of prompts and returns 
        the model's sequential responses.
        """
        pass
