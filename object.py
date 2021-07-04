from dataclasses import dataclass


@dataclass(frozen=True)
class Object:
    name: str
