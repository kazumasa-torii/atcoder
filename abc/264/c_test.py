"""

"""
import sys
import time
from io import StringIO
from tkinter import W
from typing import List

_INPUT = """\
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
2 3
6 8 9
16 18 19

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

    for hs in range(1<<h1):
        for ws in range(1<<w1):
            Is, Js = [], []
            for i in range(h1):
                if (hs>>i) & 1:Is.append(i)
            for j in range(w1):
                if (ws>>j) & 1:Js.append(j)

            if len(Is) != h2: continue
            if len(Js) != w2: continue

            c = [[0] * w2 for i in range(h2)]
            for i in range(h2):
                for j in range(w2):
                    c[i][j] = a[Is[i]][Js[j]]
            if b == c:
                print('Yes')
                exit()
    print('No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
