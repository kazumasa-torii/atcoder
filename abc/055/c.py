import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    m -= n*2
    cnt = m // 4
    print(n + cnt)
    return

if __name__ == '__main__':
    main()