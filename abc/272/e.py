import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    for i in range(m):
        for j in range(n, 0, -1):
            a[j] += j
        tmp = set(a[1:])
        if 0 not in tmp: print(0)
        elif 1 not in tmp: print(1)
        elif 2 not in tmp: print(2)
        elif 3 not in tmp: print(3)
        elif 4 not in tmp: print(4)
        elif 5 not in tmp: print(5)
        elif 6 not in tmp: print(6)
        elif 7 not in tmp: print(7)
        elif 8 not in tmp: print(8)
        elif 9 not in tmp: print(9)

if __name__ == '__main__':
    main()