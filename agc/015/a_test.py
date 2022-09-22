import sys
import time
from io import StringIO

_INPUT = """\
1 3 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)
from itertools import combinations_with_replacement
def main():
    n, a, b = map(int, input().split())
    if n == 1 and a == b: exit(print(1))
    elif a > b: exit(print(0))
    ans = set()
    for i in combinations_with_replacement(range(a, b + 1), b-a):
        ans.add(sum(i))
    print(len(ans))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
