from typing import Callable
import time

def elapsed_time(fn: Callable, *n, text: str=None) -> float:
    start_time = time.time()
    fn(*n)
    end_time = time.time()
    el = end_time - start_time
    if text:
        print(text, el)
    return el
