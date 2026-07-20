from app.core import App
from app.config import get_config


async def test_run_prints_version(capsys):
    await App(get_config()).run()
    out = capsys.readouterr().out
    assert "Version:" in out
    assert "Project root:" in out
