import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    def dfs(n):
        if memo[n]: return
        memo[n] = True
        if n == y:
            ans.append(n) 
            return True
        for next_n in g[n]:
            result = dfs(next_n)
            if result: 
                ans.append(n) 
                return True
        return False
    n, x, y = map(int, input().split())
    memo = [False] *  (n + 1)
    ans = []
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    dfs(x)
    print(*reversed(ans))
    return

if __name__ == '__main__':
    main()