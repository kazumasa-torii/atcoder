import sys
input = sys.stdin.readline

def main():
    A, B, T = map(int,input().split())
    T = T + 0.5
    kosu = T // A
    print(int(kosu * B))

main()
