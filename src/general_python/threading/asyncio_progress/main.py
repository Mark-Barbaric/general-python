# SuperFastPython.com
# example of showing the progress of tasks using a callback
import random
import asyncio
 
# callback function to show the progress of tasks
def progress(task):
    # report progress of the task
    print('.', end='')
 
# coroutine task
async def work():
    # simulate effort
    await asyncio.sleep(random.random() * 10)
 
# main coroutine
async def main():
    # create and schedule many tasks
    tasks = [asyncio.create_task(work()) for _ in range(20)]
    # add done callback function to all tasks
    for task in tasks:
        task.add_done_callback(progress)
    # wait for all tasks to complete
    _ = await asyncio.wait(tasks)
    # report final message
    print('\nAll done.')
 
# run the asyncio program

if __name__ == "__main__":
    asyncio.run(main())