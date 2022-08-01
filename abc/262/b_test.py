from distutils.spawn import spawn
import sys
import time
from io import StringIO

_INPUT = """\
5 6
1 5
4 5
2 3
1 4
3 5
2 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or i == k:continue
                if k in g[i] and j in g[k] and i in g[j]:
                    ans += 1
    print(int(ans / 6))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
