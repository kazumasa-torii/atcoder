"""
グラフというか三角の求め方みたいな感じ…。
ただ理解できないのでもう少し考えていく…。
"""

import sys
input = sys.stdin.readline
def main():
    # 角ABC（角度は時計回りに測る）が180度未満なら true
    def angle(a, b, c):
        return (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0]) > 0

    ax, ay, bx, by, cx, cy, dx, dy = map(int, open(0).read().split())
    a = (ax, ay)
    b = (bx, by)
    c = (cx, cy)
    d = (dx, dy)

    if angle(b, a, d) and angle(c, b, a) and angle(d, c, b) and angle(a, d, c):
        print('Yes')
    else:
        print('No')
    return

if __name__ == '__main__':
    main()
