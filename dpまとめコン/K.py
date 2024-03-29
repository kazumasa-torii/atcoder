"""
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
2 4
2 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [False] * (k+1)
    for i in range(1, k+1):
        for j in a:
            if i-j < 0:
                break
            if dp[i-j] == False:
                dp[i] = True
                break
        print(dp)

    print("First" if dp[k] else "Second")
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
