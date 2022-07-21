import sys
input = sys.stdin.readline
from collections import Counter
def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    cnt = Counter(c[:k])
    ans = len(cnt)
    for i in range(k, n):
        l = c[i-k]
        r = c[i]
        cnt[l] -= 1
        cnt[r] += 1
        if cnt[l] == 0:
            del cnt[l]
        ans = max(ans, len(cnt))
    print(ans)
    return

if __name__ == '__main__':
    main()
