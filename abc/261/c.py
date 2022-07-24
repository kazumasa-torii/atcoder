import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    n = int(input())
    dic = defaultdict(int)
    for _ in range(n):
        tmp = input().strip()
        if dic[tmp] != 0:
            print(f'{tmp}({dic[tmp]})')
            dic[tmp] += 1
        else:
            dic[tmp] += 1
            print(tmp)
    return

if __name__ == '__main__':
    main()
