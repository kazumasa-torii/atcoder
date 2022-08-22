"""
累積和して二分探索

1. 累積和を作っておく
1. 結局そこから目的に数になっているものが存在するか確認する
1. あればYes なければNo を出力する
"""
import sys
input = sys.stdin.readline
def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    acc = [0]
    for i in range(n): acc.append(acc[-1]+a[i])
    acc = set(acc)

    for x in acc:
        if x+p in acc and x+p+q in acc and  x+p+q+r in acc: exit(print('Yes'))
    print('No')
    return

if __name__ == '__main__':
    main()
