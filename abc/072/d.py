import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if a[i] == i+1:
            s += 1
            if i == n-1:
                a[i-1], a[i] = a[i], a[i-1]
            else:
                a[i+1], a[i] = a[i], a[i+1]
    print(s)
    return

if __name__ == '__main__':
    main()