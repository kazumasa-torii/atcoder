import sys
input = sys.stdin.readline
def main():
    n, a, b = map(int, input().split())
    if a == 0:exit(print(0))
    if b == 0:exit(print(n))
    ab = a + b
    ans = (n // ab) * a
    rem = n % ab
    ans += min(rem, a)
    print(ans)
    return

if __name__ == '__main__':
    main()
