import sys
import time
from io import StringIO

_INPUT = """\
4 2 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, a, b = map(int,input().split())
    dp = [False] * (n+1)
    for i in range(1, n+1):
        for j in a:
            if i-j < 0:
                break
            if dp[i-j] == False:
                dp[i] = True
                break
        print(dp)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
