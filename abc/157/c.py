"""
listが小さい順ということを生かした対応
ただちょっと納得いかない
"""
import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    li = []
    for _ in range(m):
        x, y = map(int, input().split())
        li.append([x-1, str(y)])
    
    for i in range(1000):
        i = str(i)
        if n != len(i): continue

        flag = True
        for x, y in li:
            if i[x] != y: flag = False
        if flag:exit(print(i))
    print(-1)
    return

if __name__ == '__main__':
    main()