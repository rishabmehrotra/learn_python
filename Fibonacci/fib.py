from sys import argv
from typing import Dict

def fibsum(n : int) -> int: #--> Function only accepts integer
    if n not in memo: # base case
        fibs.append(n)
        memo[n] = fibsum(n - 1) + fibsum(n - 2)
    return(memo[n]) # recursive case
"""
def fib6(n: int) -> Generator[int, None, None]::
    yield 0 # special case
    if n > 0: yield 1 # special case
    last: int = 0 # initially set to fib(0)
    next: int = 1 # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next # main generation step
"""

if __name__ == "__main__":
    memo: Dict[int, int] = {0 : 0, 1 : 1}
    fibs = [0 , 1]
    script, number = argv
    print(fibsum(int(number)))
    #for i in fib6(int(number)):
        #print(i,end=", ")
    print("")
    fibs.sort()
    print(fibs)
    print(','.join(str(i) for i in memo.values()))