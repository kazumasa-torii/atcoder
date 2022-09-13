"""
全部の回転したときを計算するのではなくて
料理がi回回転したときにプラスされる箇所を把握しておく

1. 回転する回数分のリストを用意
1. 料理の番号と席の人の番号が一致する箇所を計算する Pi(席の人)-i(料理の位置)
1. そこからmodを取ってlistに追加
1. listの中で一番大きなものを出力
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