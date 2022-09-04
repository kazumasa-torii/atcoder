import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    acc = [0]
    for i in range(n): acc.append(acc[-1]+a[i])
    now = 0
    si = [0] * (n-m+1)
    for i in range(m): now += a[i]*(i+1)
    si[0] = now
    for i in range(n-m+1):
        si[i] = si[i-1]+m*a[m+i-1]-(acc[m+i-1]-acc[i-1])
    print(max(si))
    return

if __name__ == '__main__':
    main()