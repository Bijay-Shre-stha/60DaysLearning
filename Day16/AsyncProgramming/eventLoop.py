import asyncio
async def function2():
    print('one')
    await asyncio.sleep(1)
    await function3()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)

async def function3():
    print('two')
    await asyncio.sleep(1)
    print('three')
    await asyncio.sleep(1)

asyncio.run(function2())
