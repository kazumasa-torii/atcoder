def main():
    x = input()
    y = input()
    ix = 0
    iy = 0
    n = len(x) + len(y)
    ans = str()
    for i in range(1, n+1):
        if i % 2 != 0:
            ans += x[ix]
            ix += 1
        else:
            ans += y[iy]
            iy += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
