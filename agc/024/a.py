import sys
input = sys.stdin.readline
def main():
    a, b, c, k = map(int, input().split())
    ans = a - b
    if k % 2 != 0: ans *= -1
    print(ans)
    return

if __name__ == '__main__':
    main()
