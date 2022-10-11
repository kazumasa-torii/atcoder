import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
4
Kita 3193
Aino 3189
Fuji 3776
Okuhotaka 3190

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from operator import itemgetter
def main():
    N = int(input())
    li = []
    for _ in range(N):
        x, y = input().split()
        li.append([x, int(y)])
    li.sort(key=itemgetter(1), reverse=True)
    print(li[1][0])

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
