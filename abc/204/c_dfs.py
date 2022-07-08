"""
bfsで値が自分の都市含めどこまで行けるか試していく
すべての都市でbfsを行い行ける都市を足していく

考察はあっていた
だが実装ができていなかったのでbfsの実装やるようにする
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)

def main():
    def dfs(u):
        """
        startからbfsをして、到達可能な都市の数を返す
        """
        for v in edge[u]:
            if not seen[v]:
                # まだvを見ていないなら、vにチェックを入れて、vに行きます
                seen[v] = True
                dfs(v)

    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]  # リストのリストで辺を持ちます
    for _ in range(M):
        a, b = (x - 1 for x in map(int, input().split()))  # 0始まりにします
        edge[a].append(b)  # 辺には向きがあって、a->bだけです

    ans = 0
    for i in range(N):
        seen = [False] * N
        seen[i] = True  # スタート地点にもチェックを入れます
        dfs(i)
        print(seen)
        ans += seen.count(True)
        print(ans)

    print(ans)


if __name__ == '__main__':
    main()
