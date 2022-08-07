import sys
input = sys.stdin.readline
def main():
    n, m, x = map(int, input().split())
    maps = [0] * (n+1)
    for i in map(int, input().split()):
        maps[i] = 1
    ncost = 0
    zcost = 0
    nx = x
    zx = x
    while nx != n:
        nx += 1
        ncost += maps[nx]

    while zx != 0:
        zx -= 1
        zcost += maps[zx]

    print(min(ncost, zcost))
    return

if __name__ == '__main__':
    main()
