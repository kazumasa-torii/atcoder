import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
4 10
3 3 4 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, x = map(int, input().split())
    li = list(map(int, input().split()))
    li.insert(0, 0)
    for i in range(len(li)):
        if i == 0 or i % 2 != 0:
            continue
        li[i] -= 1
    print('Yes' if sum(li) - x <= 0  else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
