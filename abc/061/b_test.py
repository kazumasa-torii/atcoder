import sys
import time
from io import StringIO

_INPUT = """\
2 5
1 2
2 1
1 2
2 1
1 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    city = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x:int(x)-1, input().split())
        city[a].append(b)
        city[b].append(a)
    for i in city:
        print(len(i))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
