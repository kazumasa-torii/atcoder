def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':exit(print(s[i]))
    else:
        print(1)
    return

if __name__ == '__main__':
    main()
