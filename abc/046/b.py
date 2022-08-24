import sys
input = sys.stdin.readline
def main():
    n, k = map(int, input().split())
    if n == 1:exit(print(k))
    ans = k*(k-1)
    for i in range(n-2):
        ans *= k-1
    print(ans)
    return

if __name__ == '__main__':
    main()
