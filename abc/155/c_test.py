"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    n = int(input())
    dic = defaultdict(int)

    for _ in range(n):
        tmp = input()
        dic[tmp] += 1
    nums = []
    for _, i in enumerate(dic):
        nums.append(dic[i])
    m = max(nums)

    dic_sort = sorted(dic.keys(), key=lambda x: x)

    for i in dic_sort:
        if dic[i] == m:
            print(i)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
