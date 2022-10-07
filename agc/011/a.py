"""
問題文を理解できなかった
とりあえず前から貪欲に突っ込んでいくってこと？
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    n, c, k = map(int, input().split())
    t = [int(input()) for _ in range(n)]
    t.sort()
    ans = 0
    cnt = 0
    te = 0
    for i in range(n):
        if te < t[i] or cnt == c:
            ans += 1
            te = t[i] + k
            cnt = 1
        else: cnt += 1
    print(ans)
    return

if __name__ == '__main__':
    main()