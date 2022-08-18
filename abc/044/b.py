import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    dic = defaultdict(int)
    s = input().strip()
    for i in s:
        dic[i] += 1
    for idx, key in enumerate(dic):
        if dic[key] % 2 != 0:exit(print('No'))
    print('Yes')
    return

if __name__ == '__main__':
    main()
