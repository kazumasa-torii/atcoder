import sys
import time
from io import StringIO

_INPUT = """\
000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input().strip()
    ans = 0
    for i in list(s):
        if i == '1': ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
