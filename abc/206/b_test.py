import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
100128

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N = int(input())
    money = 1
    ans = 0
    while True:
        ans += money
        money += 1
        if ans >= N:
            break
    print(money-1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
