def main():
    n, l = map(int, input().split())
    s = [input() for _ in range(n)]
    s.sort()
    print(''.join(s))
    return

if __name__ == '__main__':
    main()
