from config import config

class App:
    def __init__(self):
        pass
    
    async def flow(self):
        print(f"Version: {config.VERSION}")


    async def run(self):
        await self.flow()
        
