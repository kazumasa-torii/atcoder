from distutils.command.build_scripts import first_line_re
import sys
import time
from io import StringIO

_INPUT = """\
qqqq
81

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    k = int(input())
    n = len(s)
    tmp = s[0]
    ans = 0
    cnt = 1
    firstCnt = 0
    for i in range(1, n):
        if tmp == s[i]:
            cnt += 1
        else:
            ans += cnt // 2
            if firstCnt == 0: firstCnt = cnt
            cnt = 1
        tmp = s[i]
    ans += cnt // 2
    ans = ans * k
    if firstCnt == 0 and cnt % 2 == 1:
        ans += k // 2
    elif s[0] == s[-1] and firstCnt % 2 == 1 and cnt % 2 == 1:
        ans += k - 1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')