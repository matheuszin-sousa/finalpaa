from utils import elapsed_time


def classic_fibonacci(n:int) -> int:
    if n == 1 or n == 0:
        return n
    return classic_fibonacci(n-1) + classic_fibonacci(n-2)

def topdown_fibonacci(n: int, table:dict={}) -> int:
    if n == 1 or n==0:
        return n
    try:
        return table[n]
    except:
        table[n] = topdown_fibonacci(n-1) + topdown_fibonacci(n-2)
        return table[n]
    
def bottomup_fibonacci(n:int, table:dict = {})->int:
    table[0] = 0
    table[1] = 1
    for cont in range(2, n + 1):
        table[cont] = table[cont - 1] + table[cont - 2]
    return table[n] 

def run_fibos() -> None:
    results_classic = []
    results_td = []
    results_bu = []
    for i in range(41):
        r = elapsed_time(classic_fibonacci, i,text=f"Classic fibo time with {i}: ")
        results_classic.append(r)
        r = elapsed_time(topdown_fibonacci, i, text=f"Top Down fibo time with {i}: ")
        results_td.append(r)
        r = elapsed_time(bottomup_fibonacci, i, text=f"Bottom Up fibo time with {i}: ")
        results_bu.append(r)

    return (results_classic, results_td, results_bu)
