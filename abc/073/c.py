import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    n = int(input())
    dic = defaultdict(int)
    for _ in range(n):
        dic[int(input())] += 1
    cnt = 0
    for i, v in enumerate(dic):
        if dic[v] % 2 != 0:cnt += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()