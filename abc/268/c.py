"""
よく理解していないので再度やる
"""
import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0]*n
    for i in range(n):
        for j in range(3):
            cnt[(a[i]-1-i+j+n)%n] += 1
    ans = 0
    for i in range(n):
        ans = max(ans, cnt[i])
    print(ans) 
    return

if __name__ == '__main__':
    main()