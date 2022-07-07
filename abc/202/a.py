import sys
input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

def main():
    a, b, c = map(int, input().split())
    si = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    print(si[a] + si[b] + si[c])
    return

main()
