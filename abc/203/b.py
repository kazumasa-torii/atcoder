import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    li = []
    for i in range(1, N+1):
        for j in range(1, K+1):
            li.append(int(str(i) + '0' + str(j)))
    print(sum(li))
    return

main()
