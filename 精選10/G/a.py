import sys
input = sys.stdin.readline
import heapq
def main():
    n = int(input())
    a = list(map(lambda x: -int(x), input().split()))
    heapq.heapify(a)
    alice = 0
    bob = 0
    for i in range(n):
        tmp = heapq.heappop(a)
        if i % 2 == 0:alice += -(tmp)
        else:bob += -(tmp)
    print(alice - bob)
    return

if __name__ == '__main__':
    main()
