import math
def main():
    a, b, d = map(int, input().split())

    r = math.hypot(a, b)
    theta = math.atan2(b, a)
    theta += math.radians(d)

    x = math.cos(theta) * r
    y = math.sin(theta) * r
    print(x, y)

    return

main()
