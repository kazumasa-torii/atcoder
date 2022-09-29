import sys
input = sys.stdin.readline
def main():
    def exNum(x):
        return (((x + 1) * x) // 2) / x
    n, k = map(int, input().split())
    a = list(map(lambda x: exNum(int(x)), input().split()))
    ans = 0
    acc = [0]
    for i in a:
        acc.append(acc[-1]+i)
    for i in range(n+1):
        l = i
        r = i+k
        if r > n:break
        ans = max(ans, acc[r] - acc[l])
    print(ans)
    return

if __name__ == '__main__':
    main()