import sys
import time
from io import StringIO

_INPUT = """\
50 50

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:
        print("Silver")
    else:
        print("Alloy")
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
