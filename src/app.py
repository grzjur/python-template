from config import config

class App:
    def __init__(self):
        pass
    
    async def flow(self):
        print(f"Version: {config.VERSION}")
        print(f"Path Config: {config.paths.path_config}")
        print(f"File Config: {config.paths.file_config}")



    async def run(self):
        await self.flow()
        
