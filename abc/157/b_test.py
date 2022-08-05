from re import L
import sys
import time
from io import StringIO

_INPUT = """\
60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    bing = [list(map(int, input().split())) for _ in range(3)]
    pos = dict()
    for i in range(3):
        for j in range(3):
            pos[bing[i][j]] = [i, j]
    n = int(input())
    val = [[False] * 3 for _ in range(3)]
    for _ in range(n):
        tmp = int(input())
        if tmp not in pos:continue
        x, y = pos[tmp]
        val[x][y] = True

    flag = False

    # 縦と横
    for i in range(3):
        one, two = [], []
        for j in range(3):
           one.append(val[i][j])
           two.append(val[j][i])
        if all(one) or all(two):
            flag = True
            break

    # 斜め
    l = [val[0][0], val[1][1], val[2][2]]
    r = [val[2][0], val[1][1], val[2][0]]

    if all(l) or all(r): flag = True
    print('Yes' if flag else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
