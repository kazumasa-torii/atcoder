"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
10
10 10 10 10 20 20 20 30 30 30 30

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    dic = defaultdict(int)
    n = int(input())
    for i in map(int,input().split()):
        dic[i] += 1
    
    ans = []
    for i, v in enumerate(dic):
        if dic[v] >= 2:ans.append([v, dic[v]])
    ans.sort(reverse=True)
    if len(ans) >= 1: 
        if ans[0][1] >= 4: print(ans[0][0] * ans[0][0])
        elif len(ans) >= 2: print(ans[0][0]*ans[1][0])
    else:print(0)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
