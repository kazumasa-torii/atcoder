import sys
input = sys.stdin.readline
def main():
    n, t = map(int, input().split())
    li = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        tmp = abs(li[i] - li[i-1])
        ans += t if tmp > t else tmp
    ans += t
    print(ans) 
    return

if __name__ == '__main__':
    main()