import sys
import time
from io import StringIO

_INPUT = """\
..........
..........
..........
..........
...######.
...######.
...######.
...######.
..........
..........

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    li = []
    a, b, c, d = -1, -1, -1, -1
    for i in range(10):
        tmp = input()
        li.append(tmp)
        if tmp.find("#") == -1: continue
        if a == -1: a = i+1
        if c == -1: c = tmp.index("#") + 1
        if d == -1: d = tmp.rfind("#") + 1
    
    for i in range(9, -1, -1):
        tmp = li[i]
        if tmp.find("#") == -1: continue
        if b == -1: b = i+1
    print(a,b)
    print(c,d)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
