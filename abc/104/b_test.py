import sys
import time
from io import StringIO

_INPUT = """\
ACoder

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    n = len(s)
    cnt = 0
    Ccnt = 0
    if s[0] != 'A':exit(print('WA'))
    for i in range(n):
        if s[i].islower():cnt += 1
    for i in s[2:-1]:
        if i == 'C': Ccnt += 1
    print('AC' if Ccnt == 1 and cnt == n-2 else 'WA')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
