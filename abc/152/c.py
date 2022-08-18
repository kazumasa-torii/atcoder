import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    num_min = int(1e19)
    for i in a:
        num_min = min(num_min, i)
        if i == num_min: ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
