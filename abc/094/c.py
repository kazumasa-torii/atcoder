import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    for i in range(n):
        if a[i] < b[n//2]:print(b[n//2])
        else: print(b[n//2-1])
    return

if __name__ == '__main__':
    main()