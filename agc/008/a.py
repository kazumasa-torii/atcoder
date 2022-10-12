import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    x, y = map(int, input().split())
    if abs(x) < abs(y):
        ans = abs(y) - abs(x)
        if x < 0 or y < 0:ans += 1
        if x < 0 and y < 0: ans += 1
    else:
        ans = abs(x) - abs(y)
        if x > 0 or y > 0:ans += 1
        if x > 0 and y > 0: ans += 1
    print(ans)

    return

if __name__ == '__main__':
    main()