"""
dp[i][j]: Tの先頭からi個目までを組み合わせて、jを作れるかどうか
dp[0][0] = True で初期化します。（何も使わなくても0は作れる）
作れる値の範囲は0からS=sum(T)なので、DP配列は(N+1)×(S+1)にします
先頭から1個、T[0]を使う場合は dp[1][j]
先頭から2個、T[0]とT[1]を使う場合は dp[2][j] です

片方のオーブンを使った料理を決めたらもう片方は自動で決まる
そしてそこで0～S分までそれぞれの値をTの配列から選んだ値を作成していく
そこでS-iと取り出した合計値を比べてmaxを取り今までの値のminを取り最終的に最小値を取得していく

1.配列のsumを取得しておく
1.dpを作成して配列からできる値を予め計算しておく
1.それを配列のsumから差し引いて残りとくらべてmaxを取る
1.maxを取ったらansとのminを行い最小値を取得する
1.各値でこれを行い最終的に両方のオーブンを使用した場合の最小時間を取得する
"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
9
3 14 15 9 26 5 35 89 79

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N = int(input())
    T = list(map(int, input().split()))
    S = sum(T)

    dp = [[False] * (S + 1) for _ in range(N+1)]
    dp[0][0] = True

    for i in range(N):
        t = T[i]
        for j in range(S+1):
            if dp[i][j]:
                dp[i+1][j] = True
            if j - t >= 0 and dp[i][j-t]:
                dp[i+1][j] = True
    ans = 10 ** 10

    for i in range(S+1):
        if dp[N][i]:
            score = max(i, S-i)
            ans = min(ans, score)
    print(ans)
    return
main()
print(f'[Sec] {str(time.time() - StartTime)}')
