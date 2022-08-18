import sys
input = sys.stdin.readline
def main():
    a, b, c, x, y = map(int, input().split())
    ac = min(c*2, a+b)
    ans = 0
    while x > 0 and y > 0:
        ans += ac
        x -= 1
        y -= 1
    if x > 0:ans += min(ac, a) * x
    else:ans += min(ac, b) * y
    print(ans)
    return

if __name__ == '__main__':
    main()
