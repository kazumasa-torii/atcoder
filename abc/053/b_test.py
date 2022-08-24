import sys
import time
from io import StringIO

_INPUT = """\
HASFJGHOGAKZZFEGA

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    n = len(s)
    ai = int(1e19)
    zi = 0
    for i in range(n):
        if s[i] == 'A':
            ai = min(ai, i)
        if s[i] == 'Z':
            zi = max(zi, i)
    print(zi - (ai-1))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
