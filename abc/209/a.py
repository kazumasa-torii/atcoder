import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    ans = 0
    for i in range(1, b+1):
        if i >= a:
            ans += 1

    print(ans)
    return

if __name__ == '__main__':
    main()
