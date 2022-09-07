import sys
import time
from io import StringIO

_INPUT = """\
abaababaab

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    s = list(input())
    dic = defaultdict(int)
    for i in s: dic[i] += 1

    for i, v in enumerate(dic):
        if dic[v] % 2 != 0: flag = 

    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
