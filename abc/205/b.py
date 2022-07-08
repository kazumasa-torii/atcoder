import sys
input = sys.stdin.readline

from collections import defaultdict
def main():
    N = int(input())
    dic = defaultdict(int)
    for i in map(int, input().split()):
        dic[i] += 1

    for i, v in enumerate(dic):
        if dic[v] > 1:
            print('No')
            sys.exit()

    print('Yes')
    return

if __name__ == '__main__':
    main()
