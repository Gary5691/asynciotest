import asyncio

async def countdown_timer(n: int):
    while n > 0:
        print(f'{n} seconds remaining')
        await asyncio.sleep(1)
        n -= 1
    print('Countdown complete!')

# Start the timer in the background
async def main():
    task = asyncio.create_task(countdown_timer(5))
    print('Countdown timer started')
    await asyncio.sleep(1)
    print('Doing some other work...')
    await asyncio.sleep(3)
    print('Finished other work')
    await task

asyncio.run(main())
