import time
import asyncio
async def asyncioHello():
    await asyncio.sleep(2)
    print("Hello World!")

async def main():
    for i in range(4):
        print("\nIteration: ", i)
        print("Started at ", time.strftime("%X"))

        await asyncioHello()

        print("Finished at ", time.strftime("%X"))

asyncio.run(main())
