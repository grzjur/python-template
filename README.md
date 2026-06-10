# Python Project Template

A minimal, modern Python project template managed entirely with [uv](https://docs.astral.sh/uv/). It provides a proper `src/` package layout, configuration via Pydantic Settings, an async-first application skeleton, tests, and linting — nothing more.

## Features

- **uv-only workflow** — one tool for Python, virtualenv, dependencies, and lockfile (`pyproject.toml` + `uv.lock`)
- **src layout** — a real installable package (`src/app/`) with absolute imports and a CLI entry point
- **Configuration management** — Pydantic Settings reading from `.env`, with centralized `Paths`
- **Async-first** — `asyncio` application skeleton
- **Tests** — pytest + pytest-asyncio with working examples
- **Code quality** — ruff for linting and formatting
- **Optional AI integrations** — `.env.example` ships API key placeholders and `logfire` for observability; remove what you don't use

## Project Structure

```
python-template/
├── src/
│   └── app/
│       ├── main.py             # Entry point (uv run app)
│       ├── core.py             # Main application class
│       ├── config/
│       │   ├── settings.py     # Pydantic settings (reads .env)
│       │   └── paths.py        # Centralized filesystem paths
│       ├── models/             # Data models and schemas
│       └── utils/              # Utility functions and helpers
├── tests/                      # pytest test suite
├── .env.example                # Environment variables template
├── pyproject.toml              # Project metadata, deps, ruff & pytest config
├── uv.lock                     # Locked dependencies (committed)
└── LICENSE                     # MIT
```

## Quick Start

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) — that's it; uv installs Python itself if needed

### Setup

```bash
git clone git@github.com:grzjur/python-template.git
cd python-template

uv sync                  # creates .venv, installs deps + dev tools

cp .env.example .env     # optional — only if you use AI APIs

uv run app               # run the application
# or: uv run python -m app.main
```

## Development

```bash
uv run pytest              # run tests
uv run ruff check .        # lint
uv run ruff format .       # format
uv add <package>           # add a dependency
uv add --group dev <pkg>   # add a dev dependency
```

## Using This Template

When starting a new project from this template, rename the `app` package:

1. Rename the directory: `src/app/` → `src/<your_name>/`
2. In `pyproject.toml`, update the lines marked `# rename me`: `[project] name`, `[project.scripts]`, and `[tool.hatch.build.targets.wheel] packages`
3. Replace imports: `grep -rl "from app" src tests | xargs sed -i 's/from app/from <your_name>/g'`
4. Re-create the environment: `rm -rf .venv uv.lock && uv sync`
5. Update this README

## License

This project is open source and available under the [MIT License](LICENSE).
