import sys
import time
from io import StringIO

_INPUT = """\
BBW

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    S = list(input())
    ans = 0
    b = 0
    for i in S:
        if i == "W": ans += b
        else: b += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
