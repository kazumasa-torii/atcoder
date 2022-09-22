import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    cd = [list(map(int, input().split())) for _ in range(m)]
    for i in range(n):
        a, b = ab[i]
        tmp = []
        for j in range(m):
            c, d = cd[j]
            tmp.append(abs(a-c)+abs(b-d))
        print(tmp.index(min(tmp)) + 1)
    return

if __name__ == '__main__':
    main()