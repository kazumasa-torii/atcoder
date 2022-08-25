import sys
import time
from io import StringIO

_INPUT = """\
3
apple
orange
apple
1
grape

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    dic = defaultdict(int)
    ans = 0
    n = int(input())
    for _ in range(n):
        s = input()
        dic[s] += 1
    m = int(input())
    for _ in range(m):
        s = input()
        dic[s] -= 1
    
    for i, v in enumerate(dic):
        ans = max(ans, dic[v])
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
