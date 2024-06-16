import asyncio

async def function1():
    print("Function 1 is called")
    await asyncio.sleep(1)
    print("Function 1 is done")

async def function2():
    print("Function 2 is called")
    await asyncio.sleep(1)
    print("Function 2 is done")

async def function3():
    print("Function 3 is called")
    await asyncio.sleep(1)
    print("Function 3 is done")

async def main():
    tasks = [
        asyncio.create_task(function1()),
        asyncio.create_task(function2()),
        asyncio.create_task(function3())
    ]
    await asyncio.gather(*tasks)
    print("All functions are done")

asyncio.run(main())