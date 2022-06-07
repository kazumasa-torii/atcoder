import sys
input = sys.stdin.readline

def main():
    X, Y, Z, K = map(int,input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    B = list(map(int, input().split()))
    B.sort(reverse=True)
    C = list(map(int, input().split()))
    C.sort(reverse=True)
    tmp = []
    for i in range(X):
        for j in range(Y):
            tmp.append(A[i] + B[j])
    tmp.sort(reverse=True)
    ans = []
    for i in tmp[:K]:
        for j in range(Z):
            ans.append(i+C[j])
    ans.sort(reverse=True)
    for i in ans[:K]:
        print(i)

main()
