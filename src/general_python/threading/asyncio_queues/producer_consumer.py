# SuperFastPython.com
# example of using an asyncio queue
from random import random
import asyncio

# change this to alter behavior between consumer and producer
MAX_QUEUE_SIZE = 10

# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        # add to the queue
        print(f"Producer: put {value} at count: {i}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
 
# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        print(f"Consumer: retrieved {item}")
        # check for stop signal
        if item is None:
            break
        # report
    # all done
    print('Consumer: Done')
 
# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue(MAX_QUEUE_SIZE)
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
 
# start the asyncio program
asyncio.run(main())