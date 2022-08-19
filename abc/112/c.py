import sys
input = sys.stdin.readline
def main():
    N = int(input())
    height_dat = [list(map(int, input().split())) for _ in range(N)]

    for x, y, h in height_dat:
        if h == 0: continue
        px, py, ph = x, y, h
        break

    for cx in range(101):
        for cy in range(101):
            ch = ph + abs(px - cx) + abs(py - cy)
            for x, y, h in height_dat:
                predict = max(0, ch - abs(x - cx) - abs(y - cy))
                if h != predict: break
            else: print(cx, cy, ch)
    return

if __name__ == '__main__':
    main()
