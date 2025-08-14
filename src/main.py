from app import App
import asyncio

async def main():
    try:
        app = App()
        await app.run()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
