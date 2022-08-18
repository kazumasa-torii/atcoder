import sys
input = sys.stdin.readline
import heapq
def main():
    n = int(input())
    a = list(map(lambda x: int(x) * -1, input().split()))
    heapq.heapify(a)
    one, two = [], []
    idx = 0
    while a:
        tmp = heapq.heappop(a)
        if idx % 2 == 0: one.append(-tmp)
        else: two.append(-tmp)
        idx += 1
    print(abs(sum(one) - sum(two)))
    return

if __name__ == '__main__':
    main()
