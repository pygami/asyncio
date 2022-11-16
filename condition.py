import asyncio

async def worker(condition, tasks):
    async with condition:
        while not tasks:
            await condition.wait()
        task = tasks.pop(0)
    await task

async def main():
    condition = asyncio.Condition()
    tasks = [asyncio.sleep(i) for i in range(1, 6)]
    worker_task = asyncio.create_task(worker(condition, tasks))
    await asyncio.sleep(2)  # Simulating some work
    async with condition:
        condition.notify()
    await worker_task

asyncio.run(main())
