"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
111111111111113
157

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':exit(print(s[i]))
    else:
        print(1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
