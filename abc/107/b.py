def main():
    h, w = map(int,input().split())
    maps = [[True if i == '.' else False for i in list(input())] for _ in range(h)]
    # 横方向
    deleteList = []
    for i in range(h):
        if all(maps[i]):deleteList.append(i)
    for i in reversed(deleteList):
        del maps[i]
        h -= 1
    
    # 縦方向
    deleteList = []
    for j in range(w):
        tmp = []
        for i in range(h):
            tmp.append(maps[i][j])
        if all(tmp):deleteList.append(j)
    for j in reversed(deleteList):
        for i in range(h):
            del maps[i][j]
        w -= 1
    for i in range(h):
        ans = str()
        for j in range(w):
            ans += "." if maps[i][j] else "#"
        print(''.join(ans))
    return

if __name__ == '__main__':
    main()