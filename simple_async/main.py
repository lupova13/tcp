import time
import asyncio
from threading import Thread


class SyncTesting:
    def __init__(self):
        self._is_running = False

    def start(self):
        self._is_running = True
        print(f'Starting to run')
        self._run()

    def stop(self):
        print('Stop called')
        self._is_running = False

    def _run(self):
        counter: int = 0
        while self._is_running:
            print(f'Still running. Counter = {counter}')
            counter += 1
            time.sleep(5)


def start_task(item: SyncTesting):
    print(f'Start sync testing')
    item.start()


def stop_task(item: SyncTesting):
    print(f'Stop  sync testing')
    item.stop()


if __name__ == '__main__':
    test = SyncTesting()
    start_thread = Thread(target=start_task, args=(test,))
    print(f"started at {time.strftime('%X')}")
    start_thread.start()
    time.sleep(10)
    stop_thread = Thread(target=stop_task, args=(test,))
    stop_thread.start()
    start_thread.join()
    stop_thread.join()
    print(f"finished at {time.strftime('%X')}")



