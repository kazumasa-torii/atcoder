import sys
sys.setrecursionlimit(10**6)
def main():
    def dfs(x, y):
        if x < 0: return [x+1, y]
        if x >= h: return [x-1, y]
        if y < 0: return [x, y+1]
        if y >= w: return [x, y-1]
        if memo[x][y]: return [-1, -1]
        memo[x][y] = True
        tx, ty = dic[maps[x][y]]
        x += tx
        y += ty
        return dfs(x,y)
    h, w = map(int, input().split())
    maps = [input() for _ in range(h)]
    memo = [[False] * w for _ in range(h)]
    dic = {'U':[-1, 0], 'D':[1, 0], 'R':[0, 1], 'L':[0, -1]}
    ans = dfs(0, 0)
    if ans[0] != -1 and ans[1] != -1:print(ans[0]+1, ans[1]+1)
    else:print(-1)
    return

if __name__ == '__main__':
    main()
