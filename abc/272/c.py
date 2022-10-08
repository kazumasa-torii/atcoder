import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        even = False
        odd  = False
        if a[0] % 2 == 0:even = True
        else: odd = True
        if a[1] % 2 == 0:even = True
        else: odd = True
        if even and odd: exit(print(-1))
        else: exit(print(sum(a)))
    ma = max(a)
    if ma % 2 == 0:
        for i in reversed(a[:n-1]):
            if i % 2 == 0:
                one = ma+i
                break
        two = 0
        for i in reversed(a[:n-1]):
            if i % 2 == 1:
                two += i
                break
        for i in reversed(a[:n-1]):
            if i % 2 == 1 and two != i:
                two += i
                break
        print(max(one, two))
    else:
        for i in reversed(a[:n-1]):
            if i % 2 == 1:
                one = ma+i
                break
        two = 0
        for i in reversed(a[:n-1]):
            if i % 2 == 0:
                two += i
                break
        for i in reversed(a[:n-1]):
            if i % 2 == 0 and two != i:
                two += i
                break
        print(max(one, two))
    return

if __name__ == '__main__':
    main()