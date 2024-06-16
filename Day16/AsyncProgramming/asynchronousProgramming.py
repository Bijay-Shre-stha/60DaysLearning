import asyncio

async def function1():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(function1())



