import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        item = f"Item {i}"
        await queue.put(item)
        print(f"Produced: {item}")

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")

async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    await producer_task
    await queue.put(None)  # Signal consumer to stop
    await consumer_task

asyncio.run(main())
