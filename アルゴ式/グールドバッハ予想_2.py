def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

def main():
    num = int(input())
    for i in range(num):
        if is_prime(i):
            if is_prime(num-i):
                print(i)
                break

    return

if __name__ == '__main__':
    main()
