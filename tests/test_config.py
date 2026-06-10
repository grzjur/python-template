from pathlib import Path

from app.config import config, get_config


def test_config_is_cached_singleton():
    assert get_config() is get_config()


def test_version_is_set():
    assert isinstance(config.VERSION, str)
    assert config.VERSION


def test_base_dir_points_at_project_root():
    assert isinstance(config.paths.base_dir, Path)
    assert (config.paths.base_dir / "pyproject.toml").exists()
