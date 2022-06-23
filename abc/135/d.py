"""
sortして愚直に全探索できるか考える
その後に難しそうであれば下記アルゴリズムを考える

共通
全探索,二部探索,累積和,いもす法,順列全探索,区間スケジューリング,貪欲法

グラフ関係
DFS,BFS,ダイクストラ法,ワーシャルフロイド法,トポロジカルソート

DP
区間,bit,ナップサック,桁

数学
約数,素数判定法,mod,組み合わせ,幾何

その他
クラスカル法,木,Union-find
"""
def main():
    # s = input()
    s = '??2??5'
    l = len(s)
    mod = 10 ** 9 + 7

    N = 13
    dp = [[0] * N for _ in range(l)]
    dp[0][0] = 1

    for i in range(l):
        if s[i] == '?':
            for j in range(10):
                for k in range(N):
                    dp[i+1][(k*10+j)%N] += dp[i][k] % mod
        else:
            for k in range(N):
                dp[i+1][(k*10+int(s[i]))%N] += dp[i][k] % mod

    print(dp[-1][5]%mod)

    return

main()
