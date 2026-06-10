from pathlib import Path

from pydantic import BaseModel, Field


def _project_root() -> Path:
    # src/app/config/paths.py -> parents[3] == repo root; assumes editable install
    return Path(__file__).resolve().parents[3]


class Paths(BaseModel):
    base_dir: Path = Field(default_factory=_project_root)

    @property
    def data_dir(self) -> Path:
        return self.base_dir / "data"
