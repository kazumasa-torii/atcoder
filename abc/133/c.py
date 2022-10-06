import sys
input = sys.stdin.readline
def main():
    mod = 2019
    l, r = map(int, input().split())
    ans = int(1e19)
    if r-l == 1: exit(print((l*r)%mod))
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            ans = min(ans, (i*j)%mod)
            if ans == 0:exit(print(0))
    print(ans)
    return

if __name__ == '__main__':
    main()