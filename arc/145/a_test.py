import sys
import time
from io import StringIO

_INPUT = """\
4
ABAB

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    s = input().strip()
    if n % 2 == 0:
        nibu = int(n / 2)
        one = s[:nibu]
        two = s[nibu:]
    else:
        nibu = int(n / 2)
        one = s[:nibu]
        nibu += 1
        two = s[nibu:]
    if one == two[::-1]:
        print('Yes')
    else:
        dic = dict()
        for i in ('A','B'):
            dic[i] = 0

        for i in range(n):
            dic[s[i]] += 1

        if dic['A'] == dic['B']:
            print('No')
        else:
            print('Yes')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
