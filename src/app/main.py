import asyncio

from app.core import App


async def main() -> None:
    app = App()
    await app.run()


def cli() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    cli()
