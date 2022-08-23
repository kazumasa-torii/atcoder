import sys
import time
from io import StringIO

_INPUT = """\
NSNNSNSN

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = set(list(input()))
    flag = True
    if 'N' in s:
        if 'S' not in s:flag = False
    if 'E' in s:
        if 'W' not in s:flag = False
    if 'W' in s:
        if 'E' not in s:flag = False
    if 'S' in s:
        if 'N' not in s:flag = False
    print('Yes' if flag else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
