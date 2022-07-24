import sys
input = sys.stdin.readline
def main():
    a, b, c, d = map(int, input().split())
    l = max(a, c)
    r = min(b, d)
    print(r-l if r-l > 0 else 0)
    return

if __name__ == '__main__':
    main()
