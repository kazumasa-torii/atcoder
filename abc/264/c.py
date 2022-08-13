import bdb
import sys
input = sys.stdin.readline
def main():
    ah, aw = map(int, input().split())
    a = dict()
    for _ in range(ah):
        tmp = list(map(int, input().split()))
        for i in tmp:
            if not a.get(i):
                a[i] = 1
            else:
                a[i] += 1
    bh, bw = map(int, input().split())
    b = dict()
    for _ in range(bh):
        tmp = list(map(int, input().split()))
        for i in tmp:
            if not b.get(i):
                b[i] = 1
            else:
                b[i] += 1

    for _, key in enumerate(b):
        if not a.get(key, False):exit(print('No'))
        if a[key] < b[key]:exit(print('No'))
    print('Yes')
    return

if __name__ == '__main__':
    main()
