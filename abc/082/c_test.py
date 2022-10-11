"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5
5 5 5 5 5 

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    n = int(input())
    dic = defaultdict(int)
    for i in map(int, input().split()):
        dic[i] += 1
    ans = 0
    for i, v in enumerate(dic):
        if dic[v] != v: ans += dic[v] if dic[v] < v else dic[v] - v
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
