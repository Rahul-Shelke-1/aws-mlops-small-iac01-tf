import tomllib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_project_declares_python_version() -> None:
    pyproject_path = PROJECT_ROOT / "pyproject.toml"

    with pyproject_path.open("rb") as file:
        config = tomllib.load(file)

    assert config["project"]["requires-python"]
