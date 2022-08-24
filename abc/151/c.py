"""
問題文はしっかり読みましょう問題
waしたけどacしていない場合は、カウントしない
"""
def main():
    n, m = map(int, input().split())
    ac = [False] * n
    wa = [0] * n
    for i in range(m):
        x, y = input().split()
        x = int(x) - 1
        if ac[x]: continue
        if y == 'AC': ac[x] = True
        else:wa[x] += 1
    ans = 0
    for i, j in zip(ac, wa):
        ans += i*j
    print(sum(ac), ans)
    return

if __name__ == '__main__':
    main()
