"""Shared dataclasses for skill template generation."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SkillConfig:
    """Declarative configuration for a single skill template."""

    name: str
    depends_on: list[str] = field(default_factory=list)
    extra_context: dict[str, str] = field(default_factory=dict)


@dataclass
class TopicConfig:
    """Configuration for an upskill topic."""

    topic: str
    prompt: str
    best_practice_skill: str  # skill name constant, e.g. "mav-bp-logging"


@dataclass
class GlobalConfig:
    """Configuration shared across all skill templates."""

    extra_context: dict[str, str] = field(default_factory=dict)
