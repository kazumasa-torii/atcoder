def main():
    N: int = int(input())
    is_prime: List[int] = [True] * (N+1)
    is_prime[0], is_prime[1] = False, False
    return

if __name__ == '__main__':
    main()
