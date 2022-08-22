import sys
input = sys.stdin.readline
def main():
    x, y, n = map(int, input().split())
    ans = 0
    if n < 3:exit(print(y * n))
    if x*3 > y:
        ans = (n // 3) * y
        n %= 3
    ans += n * x
    print(ans)
    return

if __name__ == '__main__':
    main()
