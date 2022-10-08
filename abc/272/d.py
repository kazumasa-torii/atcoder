import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    def bfs(h, w, cnt):
        if h < 0 or w < 0 or h >= n or w >= n: return
        if maps[h][w] != -1: maps[h][w] = min(maps[h][w], cnt)
        maps[h][w] = cnt
        bfs(h+half, w+1, cnt+1)
        bfs(h-half, w-1, cnt+1)
        bfs(h+1, w+half, cnt+1)
        bfs(h-1, w-half, cnt+1)
        return
    n, m = map(int, input().split())
    half = m // 2
    maps = [[-1] * n for _ in range(n)]
    bfs(0, 0, 0)
    print(maps)
    return

if __name__ == '__main__':
    main()