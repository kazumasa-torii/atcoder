import sys
input = sys.stdin.readline
from operator import itemgetter
def main():
    n = int(input())
    r = []
    for i in range(n):
        x, y = input().split()
        y = int(y)
        r.append([x,-y,i+1])
    r.sort(key=itemgetter(0, 1))

    for i in range(n):
        print(r[i][2])
    return

if __name__ == '__main__':
    main()
