"""
とりあえず全部試すパターンの内容を一度考えて計算量を下げれるか試すのが大事
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
2
1 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    sy = 0
    ans = int(1e18)
    for i in range(101):
        tmp = 0
        for j in x:
            tmp += abs(j - i) ** 2
        ans = min(ans, tmp)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
