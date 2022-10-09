import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    n = int(input())
    a = [0] * 5
    dic = {"M":0,"A":1,"R":2,"C":3,"H":4}
    inList = ["M", "A", "R", "C", "H"]
    for i in range(n):
        tmp = input()
        if tmp[0] not in inList: continue
        a[dic[tmp[0]]] += 1
    ans = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                ans += a[i]*a[j]*a[k]
    print(ans)
    return

if __name__ == '__main__':
    main()