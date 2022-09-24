import sys
input = sys.stdin.readline
def main():
    ans = 0
    x, y, z = map(int, input().split())
    # 0より大きい場合
    if x > 0:
        if x < y: exit(print(x))
        if z > 0 and x > y > z: exit(print(x))
        if y < 0 : exit(print(x))
        if y < x and y < z and y > 0: exit(print(-1))
        ans = (-z + -z) + x
    # 0より小さい場合
    else:
        if x > y: exit(print(-x))
        if x < y < z and z < 0: exit(print(-x))
        if y > 0: exit(print(-x))
        if y > x and y > z and y < 0: exit(print(-1))
        ans = (z + z) + -x
    print(ans)
    return

if __name__ == '__main__':
    main()