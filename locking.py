import asyncio

async def increment(counter, lock):
    for _ in range(1000):
        async with lock:
            counter += 1

async def main():
    counter = 0
    lock = asyncio.Lock()
    tasks = [increment(counter, lock) for _ in range(4)]
    await asyncio.gather(*tasks)
    print("Counter value with Lock:", counter)

asyncio.run(main())

