import sys
import time
from io import StringIO

_INPUT = """\
abaababaab

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    while len(s) > 0:
        s = s[:-1]
        n = len(s)
        if n % 2 != 0: continue
        one = s[:n//2]
        two = s[n//2:]
        if one == two: break
    print(len(s))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
