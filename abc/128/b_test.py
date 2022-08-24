from email.errors import InvalidMultipartContentTransferEncodingDefect
import sys
import time
from io import StringIO

_INPUT = """\
6
khabarovsk 20
moscow 10
kazan 50
kazan 35
moscow 60
khabarovsk 40

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from operator import itemgetter
def main():
    n = int(input())
    r = []
    for i in range(n):
        x, y = input().split()
        y = int(y)
        r.append([x,-y,i+1])
    r.sort(key=itemgetter(0, 1))

    for i in range(n):
        print(r[i][2])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
