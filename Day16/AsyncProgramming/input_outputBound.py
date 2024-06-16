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
    await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print("All functions are done")

asyncio.run(main())
