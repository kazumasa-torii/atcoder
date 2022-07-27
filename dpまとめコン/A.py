"""
遷移の仕方を気をつける
イマイチ理解していないまま実装したので時間がかかった
○の状態から△を行い□に遷移する
みたいな感覚を理解してからじゃないとだめ
前からと後ろからの二通りを試して遷移の仕方に違和感がないか確認して進める
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
4
10 30 40 20

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    INF = int(1e18)
    n = int(input())
    li = list(map(int, input().split()))
    dp = [INF] * n
    dp[0] = 0
    for i in range(1, n):
        one, two = INF, INF
        one = min(dp[i], abs(li[i] - li[i-1]) + dp[i-1])
        if i - 2 >= 0:
            two = min(dp[i], abs(li[i] - li[i-2]) + dp[i-2])
        dp[i] = min(one, two)
    print(dp[-1])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
