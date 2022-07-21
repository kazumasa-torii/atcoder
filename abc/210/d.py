"""
1. 式の絶対値を外すようにする（混乱を招く元なので）
絶対値は値が小さい場合があるので
絶対値を取るようにしているので
常に大きい数字から小さい数字を引けば問題なくなる
1. なので位置関係を逆にしてマス目の大きい方を先に持ってくるようにする
すると以下のような式に変換できる
a[x1][y1] + c*(x1 + y1) + a[x2][y2] - c*(x2 + y2)
1. 1番目のマスを固定したら2番めのマスの決めていく
1. 以下の条件のものが最適
 * a[x2][y2] - c*x(2+y2)が最小
 * x2<=x1 and y2<=y1
1. 各マスの計算を進めていき最小値を常に取得して答えに代入しておく
1. これをリバースして順番を逆にして再度計算
1. 最終的な答えを出力

多分これはわからない
ただ考え方をもう少し理解する必要があるので進めておく
"""

import sys
input = sys.stdin.readline
def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    INF = 10 ** 10
    ans = INF
    for _ in range(2):
        dp = [[INF] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if i > 0: dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j > 0: dp[i][j] = min(dp[i][j], dp[i][j-1])
                ans = min(ans, a[i][j] + c * (i+j) + dp[i][j])
                dp[i][j] = min(dp[i][j], a[i][j] - c*(i+j))
        a.reverse()
    print(ans)
    return

if __name__ == '__main__':
    main()
