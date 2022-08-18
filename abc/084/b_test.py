import sys
import time
from io import StringIO

_INPUT = """\
1 2
7444

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b = map(int, input().split())
    x = input().strip()
    flag = True
    for i in range(len(x)):
        print(x[i].isdecimal(), i)
        if not x[i].isdecimal() and a != i:
            flag = False
            break
        if a == i and x[i].isdecimal():
            flag = False
            break
    print('Yes' if flag else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
