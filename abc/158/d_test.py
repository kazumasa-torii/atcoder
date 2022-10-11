"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
acdd
6
2 1 p
1
2 2 c
1
1
2 1 c

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
def main():
    s = input()
    q = int(input())
    a = deque(list(s))
    flag = True
    for _ in range(q):
        tmp = input()
        if tmp[0] == "1":
            flag = False if flag else True
        else:
            t, f, c = tmp.split()
            if f == "1":
                if flag:
                    a.appendleft(c)
                else:
                    a.append(c)
            else:
                if not flag:
                    a.appendleft(c)
                else:
                    a.append(c)
    print("".join(a) if flag else "".join(reversed(a)))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
