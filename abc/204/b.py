import sys
input = sys.stdin.readline
def main():
    N = int(input())
    li = list(map(int, input().split()))
    ans = 0
    for i in li:
        if i <= 10:
            continue
        ans += (i-10)
    print(ans)
    return

main()
