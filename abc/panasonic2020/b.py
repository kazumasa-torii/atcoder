import sys
input = sys.stdin.readline
def main():
    h, w = map(int, input().split())
    if h == 1 or w == 1:
        print(1)
        exit()
    ans = h * w // 2
    amari = h * w % 2
    print(ans + amari)
    return

if __name__ == '__main__':
    main()
