import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    num = []
    for i in range(n):
        num.append(list(map(int, input().split()))[1:])
    for i in range(m):
        x, y = map(int, input().split())
        print(num[x-1][y-1])
    return

if __name__ == '__main__':
    main()