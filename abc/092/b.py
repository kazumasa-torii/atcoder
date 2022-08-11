import sys
input = sys.stdin.readline
def main():
    n = int(input())
    d, x = map(int, input().split())
    ans = 0
    for _ in range(n):
        day = 1
        tmp = int(input())
        while day <= d:
            ans += 1
            day += tmp
    print(ans + x)
    return

if __name__ == '__main__':
    main()
