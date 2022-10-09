"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
atcoder

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    t = 'atcoder'
    s = input().strip()
    n = len(t)
    dic = defaultdict()
    for i in range(n): dic[t[i]] = i
    a = []
    for i in range(n): a.append(dic[s[i]])
    ans = 0
    for i in range(n):
        for j in range(i):
            if a[j] > a[i]: ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
