import sys
import time
from io import StringIO

_INPUT = """\
20 2 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def is_sum(n):
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        return sum

    ans = []
    n, a, b = map(int, input().split())
    for i in range(1, n+1):
        tmp = is_sum(i)
        if a <= tmp <= b: ans.append(i)
    print(sum(ans))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
