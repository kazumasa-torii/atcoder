import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        tmp = int(input())
        a.append(tmp)
        if tmp % 10 != 0: b.append(tmp)
    b.sort()
    sumA = sum(a)
    if sumA % 10 == 0:
        if not b: sumA = 0
        else: sumA -= b[0]
    print(sumA)
    return

if __name__ == '__main__':
    main()