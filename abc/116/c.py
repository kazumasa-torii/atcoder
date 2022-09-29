import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i-1] > a[i]:ans += a[i-1] - a[i]
    ans += a[-1]
    print(ans)
    return

if __name__ == '__main__':
    main()