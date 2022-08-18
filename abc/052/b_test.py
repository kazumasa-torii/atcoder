import sys
import time
from io import StringIO

_INPUT = """\
5
IIDID

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    s = input().strip()
    ans = 0
    tmp = 0
    for i in list(s):
        if i == 'I':tmp+=1
        else:tmp -=1
        ans = max(ans, tmp)
    print(max(ans, 0))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
