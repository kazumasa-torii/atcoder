import sys
input = sys.stdin.readline
def main():
    n, k, q = map(int, input().split())
    ans = [int(input()) for _ in range(q)]
    syo = k - q
    p = [syo for _ in range(n)]
    for i in ans:
        p[i-1] += 1

    for i in p:
        if i >= 1: print('Yes')
        else: print('No')
    return

if __name__ == '__main__':
    main()
