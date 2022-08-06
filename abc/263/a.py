import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    li = list(map(int, input().split()))
    flag = True
    dic = defaultdict(int)
    for i in li:
        dic[i] += 1
    if len(dic) != 2:
        print('No')
        exit()
    for _, i in enumerate(dic):
        if dic[i] == 2 or dic[i] == 3:continue
        flag = False
    print('Yes' if flag else 'No')
    return

if __name__ == '__main__':
    main()
