import sys
import time
from io import StringIO

_INPUT = """\
15
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
9
5 4 3 2 1 2 3 4 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    one = defaultdict(int)
    two = defaultdict(int)
    n = int(input())
    for i in map(int, input().split()):
        one[i] += 1
    m = int(input())
    for i in map(int, input().split()):
        two[i] += 1
    
    flag = True
    for i, v in enumerate(two):
        if two[v] > one[v]: flag = False
    print('YES' if flag else 'NO')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
