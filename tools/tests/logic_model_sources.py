"""Canonical cross-book source inventory for logic and model theory tests."""
from pathlib import Path


def logic_model_sources(directory: Path) -> list[Path]:
    """Preserve isolated fixtures; use both canonical books for cross-references."""
    if directory.name in {"logic_and_set_theory", "model_theory"} and directory.parent.name == "pl":
        return sorted([*directory.parent.joinpath("logic_and_set_theory").glob("*.tex"),
                       *directory.parent.joinpath("model_theory").glob("*.tex")])
    return sorted(directory.glob("*.tex"))
