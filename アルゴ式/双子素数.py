def main():
    N = int(input())
    is_prime = [True] * (N+1)

    is_prime[0], is_prime[1] = 0, 0
    for p in range(2, N+1):
        if not is_prime[p]: continue

        q = p * 2
        while q <= N:
            is_prime[q] = False
            q += p
    ans = 0
    for a in range(2, N-1):
        if is_prime[a] and is_prime[a+2]:
            ans += 1
    return ans

print(main())
