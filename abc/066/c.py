import sys
input = sys.stdin.readline
from collections import deque
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = deque()
    flag = True
    for i in range(n):
        if flag:
            b.append(a[i])
            flag = False
        else:
            b.appendleft(a[i])
            flag = True
    print(*b)
    return

if __name__ == '__main__':
    main()