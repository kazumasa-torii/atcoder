import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
4 5 2
3 2
2 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    # 座標圧縮
    def compress(ar):
        ans = list(set(ar))
        ans.sort()

        conv = dict()
        for i in range(len(ans)):
            conv[ans[i]] = i + 1
        return conv

    h, w, n = map(int, input().split())

    li = []
    a = []
    b = []

    for i in range(n):
        x, y = map(int, input().split())
        li.append([x, y])
        a.append(x)
        b.append(y)

    xconv = compress(a)
    yconv = compress(b)

    for x, y in li:
        print(xconv[x], yconv[y])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
