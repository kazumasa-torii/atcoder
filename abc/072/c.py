import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    dic = defaultdict(int)
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        dic[i-1] += 1
        dic[i] += 1
        dic[i+1] += 1
    ans = 0
    for i, v in enumerate(dic):
        ans = max(ans, dic[v])
    print(ans)
    return

if __name__ == '__main__':
    main()