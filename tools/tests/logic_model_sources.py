"""Canonical cross-book source inventory for logic and model theory tests."""
from pathlib import Path


def logic_model_sources(directory: Path) -> list[Path]:
    """Preserve isolated fixtures; use canonical books for cross-references."""
    subjects = ("logic_and_set_theory", "model_theory", "metamathematics")
    if directory.name in subjects and directory.parent.name == "pl":
        return sorted(path for subject in subjects
                      for path in directory.parent.joinpath(subject).glob("*.tex"))
    return sorted(directory.glob("*.tex"))
