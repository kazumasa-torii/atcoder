import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = [0] + list(map(int, input().split())) + [0]
    moveCost = []
    tot = 0
    for i in range(1, len(a)):
        tot += abs(a[i] - a[i-1])
        moveCost.append(abs(a[i] - a[i-1]))
        # [3, 2, 6, 1]

    for i in range(1, len(a)-1):
        tmp = tot
        tmp -= moveCost[i]
        tmp -= moveCost[i-1]
        tmp += abs(a[i-1] - a[i+1])
        print(tmp)
    return

if __name__ == '__main__':
    main()