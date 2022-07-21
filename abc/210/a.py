import sys
input = sys.stdin.readline
def main():
    n, a, x, y = map(int, input().split())
    low = n-a
    if low > 0:
        print((low * y) + (a * x))
    else:
        print(n*x)
    return

if __name__ == '__main__':
    main()
