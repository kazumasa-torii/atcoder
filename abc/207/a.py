import sys
input = sys.stdin.readline
import heapq
def main():
    li = list(map(lambda x: int(x) * -1, input().split()))
    heapq.heapify(li)
    a = heapq.heappop(li) * -1
    b = heapq.heappop(li) * -1
    print(a + b)
    return

if __name__ == '__main__':
    main()
