from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class Scenario:
    """
    Defines the world in which agents behave.
    Acts as an experiment configuration.
    """

    name: str
    domain: str

    environment: Dict[str, Any] = field(default_factory=dict)
    population: Dict[str, Any] = field(default_factory=dict)
    stimuli: List[Dict[str, Any]] = field(default_factory=list)
    policies: Dict[str, Any] = field(default_factory=dict)
    interventions: List[Dict[str, Any]] = field(default_factory=list)
    metrics: List[str] = field(default_factory=list)

    def describe(self) -> str:
        return (
            f"Scenario: {self.name} ({self.domain})\n"
            f"Environment: {list(self.environment.keys())}\n"
            f"Population rules: {list(self.population.keys())}\n"
            f"Interventions: {len(self.interventions)}"
        )
