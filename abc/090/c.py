import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    if n == 1 and m == 1: exit(print(1))
    elif n == 1: exit(print(m-2))
    elif m == 1: exit(print(n-2))
    n -= 2
    m -= 2
    print(n*m)
    return

if __name__ == '__main__':
    main()