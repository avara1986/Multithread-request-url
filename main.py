# encoding: utf-8
from multiprocessing import cpu_count
import concurrent.futures as cf
import time
import requests
import random

def send_url(count):
    '''
    data = { }
    files = { }
    response = requests.post(
        "[URL]", data=data, files=files)
    '''
    time.sleep(3)
    print(count)
    return count

def send_urls():
    with cf.ThreadPoolExecutor(8) as pool:
        res = pool.map(send_url, [i for i in range(151)])
    return len(list(res))

if __name__ == '__main__':
    t0 = time.time()

    count = send_urls()

    elapsed = time.time() - t0

    msg = '\n{} process in {:.2f}s'

    print(msg.format(count, elapsed))
