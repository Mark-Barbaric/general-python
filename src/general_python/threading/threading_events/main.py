from time import sleep
from random import random
from threading import Thread
from threading import Event


def task(event: Event, number: int):
    event.wait()
    value = random()
    sleep(value)
    print(f"Thread {number} got value {value}")


if __name__ == "__main__":
    event = Event()
    for i in range(5):
        thread = Thread(target=task, args=(event, i))
        thread.start()
    print("main thread blocking")
    sleep(2)
    event.set()
