"""

"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from math import atan2, hypot, pi

def main():
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]
    cd = [list(map(int, input().split())) for _ in range(N)]
    EPS = 10**-9
    
    def shift_angle_radius(xy):
        c = [0,0]
        for x, y in xy:
            c[0] += x
            c[1] += y
        c[0] /= len(xy)
        c[1] /= len(xy)
        xy = [(x-c[0],y-c[1]) for x,y in xy]
        angle = []
        radius = []
        for i in range(N):
            a = atan2(xy[i][1], xy[i][0])
            r = hypot(xy[i][0], xy[i][1])
            if r > EPS:
                angle.append(a)
                radius.append(r)
        return list(zip(angle, radius))

    def normalize(ar, a0):
        ar = [[a - a0,r] for a,r in ar]
        for j in range(len(ar)):
            while ar[j][0] < 0:
                if abs(ar[j][0]) < EPS:
                    ar[j][0] = 0
                    break
                ar[j][0] += 2*pi
            while ar[j][0] > 2*pi:
                if abs(ar[j][0]-2*pi) < EPS:
                    ar[j][0] = 0
                    break
                ar[j][0] -= 2*pi
        return sorted(ar)

    ar_ab = shift_angle_radius(ab)
    ar_cd = shift_angle_radius(cd)
    if len(ar_ab) != len(ar_cd):
        print('No')
        return
    if len(ar_ab) == len(ar_cd) == 0:
        print('Yes')
        return

    ar_ab = normalize(ar_ab, ar_ab[0][0])
    ar_cd = normalize(ar_cd, ar_cd[0][0])
    for i in range(len(ar_cd)):
        ar = normalize(ar_cd, ar_cd[i][0])
        for j in range(len(ar)):
            if abs(ar[j][1] - ar_ab[j][1]) > EPS:
                break
            if ar[j][1] > EPS:
                if abs(ar[j][0] - ar_ab[j][0]) < EPS or\
                    abs(ar[j][0] - ar_ab[j][0] - 2*pi) < EPS:
                    pass
                else:
                    break
        else:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
