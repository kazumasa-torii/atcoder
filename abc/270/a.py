def main():
    a, b = map(int, input().split())
    tmp = int(format(a, 'b')) | int(format(b, 'b'))
    tmp = str(tmp).zfill(3)[::-1]
    tot = 0
    point = [1, 2, 4]
    for i in range(3):
        if tmp[i] == '1': tot += point[i]
    print(tot)
    return

if __name__ == '__main__':
    main()