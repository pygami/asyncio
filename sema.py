import asyncio

async def worker_task(task_number, semaphore):
    async with semaphore:
        print(f"Task {task_number} started")
        await asyncio.sleep(1)
        print(f"Task {task_number} completed")

async def main():
    semaphore = asyncio.Semaphore(2)
    tasks = [worker_task(i, semaphore) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())
