import sys
input = sys.stdin.readline
def main():
    def multi(x):
        cnt = 0
        while n > 1:
            if x % 2 != 0:break
            x //= 2
            cnt += 1
        return cnt
    n = int(input())
    a = list(map(int, input().split()))
    multiple = {0:0, 1:0, 2:0}
    for i in range(n):
        multiple[min(multi(a[i]), 2)] += 1
    print('Yes' if multiple[0] <= multiple[2]  else 'No')
    return

if __name__ == '__main__':
    main()