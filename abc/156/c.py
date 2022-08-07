import sys
input = sys.stdin.readline
def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    sy = 0
    ans = int(1e18)
    for i in range(101):
        tmp = 0
        for j in x:
            tmp += abs(j - i) ** 2
        ans = min(ans, tmp)
    print(ans)
    return

if __name__ == '__main__':
    main()
