import sys
import time
from io import StringIO

_INPUT = """\
2B
3B
HR
3B

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    flag = [False] * 4
    for _ in range(4):
        h = input().strip()
        if h == "H":
            flag[0] = True
        if h == "2B":
            flag[1] = True
        if h == "3B":
            flag[2] = True
        if h == "HR":
            flag[3] = True
    ans = True
    for i in flag:
        if not i:
            ans = False
    print('Yes' if ans else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
