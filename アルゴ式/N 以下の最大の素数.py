def main():
    num = int(input())
    for i in range(num, 1, -1):
        flag = True
        for j in range(2, i + 1):
            if j * j > i:
                break
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i)
            break
    return

if __name__ == '__main__':
    main()
