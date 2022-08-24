def main():
    N = input()
    print(max(int(N[0])-1+9*(len(N)-1),sum(map(int,N))))
    return

if __name__ == '__main__':
    main()
