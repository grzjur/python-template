import asyncio
import sys

from pydantic import ValidationError
from app.core import App
from app.config import get_config


async def main() -> None:
    config = get_config()
    app = App(config)
    await app.run()


def cli() -> None:
    try:
        asyncio.run(main())
    except ValidationError as error:
        print(f"Invalid configuration:\n{error}", file=sys.stderr)
        raise SystemExit(2) from None


if __name__ == "__main__":
    cli()
