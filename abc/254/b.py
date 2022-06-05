import sys
input = sys.stdin.readline

def main():
    N = int(input())
    limit = N * 5
    DP = [[0] * limit for _ in range(N+1)]
    DP[0][0] = 1
    for i in range(1, N+1):
        for j in range(limit):
            if j == 0:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i-1][j] + DP[i-1][j-1]
    for i in range(len(DP)):
        if i == N:
            break
        for num in DP[i]:
            if num != 0:
                print(num, end=" ")
        print(end="\n")


main()
