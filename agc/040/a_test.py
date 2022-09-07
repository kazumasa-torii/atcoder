import sys
import time
from io import StringIO

_INPUT = """\
<>>><<><<<<<>>><

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    n = len(s)
    ans = [0] * (n+1)
    for i in range(n):
        if s[i] == '<': ans[i+1] = ans[i] + 1
    for i in range(n-1, -1, -1):
        if s[i] == '>': ans[i] = max(ans[i], ans[i+1] + 1)
    print(sum(ans))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
