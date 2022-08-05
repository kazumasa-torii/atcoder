import sys
input = sys.stdin.readline
def main():
    a, b = map(int,input().split())
    ans = 1
    cnt = 0
    while True:
        if ans >= b: break
        ans -= 1
        ans += a
        cnt += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()
