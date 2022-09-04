import sys
import time
from io import StringIO

_INPUT = """\
0000001001

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    if int(s[0]):exit(print('No'))
    r = [False] * 7
    if not int(s[6]): r[0] = True
    if not int(s[9]): r[6] = True
    if not int(s[3]): r[1] = True
    if not int(s[5]): r[5] = True
    if not int(s[1]) and not int(s[7]): r[2] = True
    if not int(s[2]) and not int(s[8]): r[4] = True
    if not int(s[0]) and not int(s[4]): r[3] = True
    n = 7
    for i in range(n):
        for j in range(i+1, n):
            if not r[i] and not r[j]:
                for k in range(i, j):
                    if r[k]:exit(print('Yes'))
    print('No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
