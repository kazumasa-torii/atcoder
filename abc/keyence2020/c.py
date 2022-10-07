import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    n, k, s = map(int,input().split())
    ans = []
    for _ in range(k):
        ans.append(s)
    for _ in range(n-k):
        ans.append(s+1)
    print(*ans) 
    return

if __name__ == '__main__':
    main()