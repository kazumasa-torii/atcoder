import sys
import time
from io import StringIO

_INPUT = """\
hheettaax

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    dic = defaultdict(int)
    s = input()
    for i in s:
        dic[i] += 1
    print(dic)
    for idx, key in enumerate(dic):
        if dic[key] % 2 != 0:exit(print('No'))
    print('Yes')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
