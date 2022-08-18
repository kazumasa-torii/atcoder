import sys
import time
from io import StringIO

_INPUT = """\
different

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    dic = dict()
    s = input().strip()
    for i in range(97, 97+26):
        dic[chr(i)] = 0

    for i in list(s):
        dic[i] += 1

    flag = True
    for _, i in enumerate(dic):
        if dic[i] > 1:
            flag = False
            break
    print('yes' if flag else 'no')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
