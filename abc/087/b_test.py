import sys
import time
from io import StringIO

_INPUT = """\

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    ans = 0
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i * 500 + j * 100 + k * 50 == x: ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()

    print(f'[Sec] {str(time.time() - StartTime)}')
