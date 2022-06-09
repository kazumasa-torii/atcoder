"""
簡単のifelse
"""
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

def main():
    N, K = map(int, input().split())
    K -= 1
    S = list(input())
    S[K] = S[K].lower()
    print(''.join(S))
main()
