import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
5
00101

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    s = input().strip()
    for i in range(n):
        if s[i] == '1':
            if i % 2 == 0:
                print('Takahashi')
                exit()
            else:
                print('Aoki')
                exit()
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
