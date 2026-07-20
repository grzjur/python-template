from app.config import Config

class App:
    def __init__(self, config: Config) -> None:
        self.config = config

    async def flow(self) -> None:
        print(f"Version: {self.config.VERSION}")
        print(f"Project root: {self.config.paths.base_dir}")

    async def run(self) -> None:
        await self.flow()
