from app.config import config


class App:
    async def flow(self) -> None:
        print(f"Version: {config.VERSION}")
        print(f"Project root: {config.paths.base_dir}")

    async def run(self) -> None:
        await self.flow()
