import asyncio
import random


list_items = []

for i in range(1,100):
    list_items.append(i)


async def countdown_timer(n: int, item: str):
    print(f'working on {item}')
    while n > 0:
        await asyncio.sleep(1)
        n -= 1
    print(f"Done with {item}")



async def main(list_items: list):
    semaphore = asyncio.Semaphore(3) # Number of tasks that can run in parallel
    tasks = []
    for item in list_items:
        await semaphore.acquire()
        task = asyncio.create_task(countdown_timer(random.randrange(1,100), item))
        task.add_done_callback(lambda t: semaphore.release())
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(main(list_items))