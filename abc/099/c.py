import sys
input = sys.stdin.readline
def main():
    def judge(n, i):
        i -= 1
        cnt = 1
        while n > 0:
            n -= i
            cnt += 1
        return cnt
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == k: exit(print(1))
    print(judge(n-k, k))
    return

if __name__ == '__main__':
    main()