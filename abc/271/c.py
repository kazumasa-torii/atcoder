"""
読みたい本があればn-1する
読みたい本がなければn-2する
そしてその数が0未満になっているなら前の本まで読めるのでそこでbreakする
"""
import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))

    setA = set(a)
    remain = n

    ans = 0
    for i in range(1, n + 1):
        if i in setA:
            remain -= 1
        else:
            remain -= 2
        
        if remain < 0:
            break
        
        ans = i

    print(ans)
    return

if __name__ == '__main__':
    main()