import sys
import time
from io import StringIO

_INPUT = """\
3 8 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, k = map(int, input().split())
    ans = set()
    for i in range(k):
        if a+i > b:break
        ans.add(a+i)
    for i in range(k-1, -1, -1):
        if b-i < a: break
        ans.add(b-i)
    ans = sorted(ans)
    for i in ans:print(i)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
