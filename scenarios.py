from dataclasses import dataclass
from typing import List

@dataclass
class Scenario:
    id: str
    category: str
    security_boundary: str
    direct_prompt: str
    multi_step_prompt: List[str]
    expected_safe_behavior: str
    unsafe_indicators: List[str]
