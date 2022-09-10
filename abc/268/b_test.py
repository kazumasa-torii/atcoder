import sys
import time
from io import StringIO

_INPUT = """\
atco
atcoder

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    t = input()
    if len(s) > len(t):exit(print('No'))
    flag = True
    for i in range(len(s)):
        if s[i] != t[i]:flag=False
    print('Yes' if flag else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
