from app.core import App


async def test_run_prints_version(capsys):
    await App().run()
    out = capsys.readouterr().out
    assert "Version:" in out
    assert "Project root:" in out
