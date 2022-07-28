import sys
input = sys.stdin.readline
from copy import deepcopy
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = deepcopy(a)
    ans.sort()
    print(a.index(ans[-2]) + 1)
    return

if __name__ == '__main__':
    main()
