import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    n = int(input())
    dic = defaultdict(int)
    for i in map(int, input().split()):
        dic[i] += 1
    ans = 0
    for i, v in enumerate(dic):
        if dic[v] != v: ans += dic[v] if dic[v] < v else dic[v] - v
    print(ans)
    return

if __name__ == '__main__':
    main()