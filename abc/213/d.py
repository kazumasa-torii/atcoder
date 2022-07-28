"""
割りとシンプルなDFSだったので実装出来なかったのは悔しい
とりあえず実装してからチョロチョロ修正するのが良かったかも

1. グラフを作ってDFS
1. 行きがけにまず配列に親を追加
1. その後に子のDFSを行って終わったら親を追加して通り道を記録する
1. あとは答えを+1ずつして答える
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
def main():
    def dfs(v, p=-1):
        ans.append(v)
        for v2 in g[v]:
            if v2 == p: continue
            dfs(v2, v)
            ans.append(v)
        return
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    ans = []
    for i in range(n):
        if not g[i]: continue
        g[i].sort()

    dfs(0)
    for i in range(len(ans)):
        ans[i] += 1
    print(*ans)
    return

if __name__ == '__main__':
    main()
