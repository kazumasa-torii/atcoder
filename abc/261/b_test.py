import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
4
-WWW
L-DD
LD-W
LDW-

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    vs = [list(input().strip()) for _ in range(n)]

    flag = True
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if vs[i][j] == 'W':
                if vs[j][i] != 'L': flag = False
            if vs[i][j] == 'L':
                if vs[j][i] != 'W': flag = False
            if vs[i][j] == 'D':
                if vs[j][i] != 'D': flag = False
    print('correct' if flag else 'incorrect')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
