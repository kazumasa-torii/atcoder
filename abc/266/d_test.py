"""
sortして愚直に全探索できるか考える
その後に難しそうであれば下記アルゴリズムを考える

共通
全探索,二部探索,累積和,いもす法,順列全探索,区間スケジューリング,貪欲法,鳩の巣原理

グラフ関係
DFS,BFS,ダイクストラ法,ワーシャルフロイド法,トポロジカルソート

DP
区間,bit,ナップサック,桁

数学
約数,素数判定法,mod,組み合わせ,幾何

その他
クラスカル法,木,Union-find
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
3
1 0 100
3 3 10
5 4 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    max_time = 0
    for i in li: max_time = max(i[0], max_time)
    position_list = [0] * (max_time + 1)
    scor_list = [0] * (max_time + 1)

    for i in li:
        t, x, a = i
        position_list[t] = x
        scor_list[t] = a

    dp = [[0] * (max_time + 1) for _ in range(5)]
    dp[0][0] = 0

    for time in range(1, max_time+1):
        for position in range(5):
            dp[position][time] = dp[position][time-1]
            if position != 0: dp[position][time] = max(dp[position][time], dp[position-1][time-1])
            if position != 4: dp[position][time] = max(dp[position][time], dp[position+1][time-1])
        dp[position_list[time]][time] += scor_list[time]
        print(dp)
    print(max(dp[i][max_time] for i in range(5)))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
