import asyncio

async def countdown(event):
    print("Countdown started")
    await asyncio.sleep(3)
    print("Countdown finished")
    event.set()

async def celebrate(event):
    print("Waiting for countdown to finish")
    await event.wait()
    print("Happy New Year!")

async def main():
    event = asyncio.Event()
    await asyncio.gather(countdown(event), celebrate(event))

asyncio.run(main())
