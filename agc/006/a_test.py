import sys
import time
from io import StringIO

_INPUT = """\
4
abcd
cdaa

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    s = input()
    t = input()
    
    ans = 2*n
    cnt = 0
    for i in range(n):
        if s[n-i-1:] == t[:i+1]:
            cnt = max(cnt, i+1)
    print(ans-cnt)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
