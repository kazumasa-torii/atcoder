import sys
input = sys.stdin.readline
import heapq
def main():
    q = int(input())
    hq = []
    s = 0
    heapq.heapify(hq)
    for _ in range(q):
        li = list(map(int, input().split()))
        if li[0] == 1:
            heapq.heappush(hq, li[1] - s)
        elif li[0] == 2:
            s += li[1]
        elif li[0] == 3:
            tmp = heapq.heappop(hq)
            print(tmp+s)
    return

if __name__ == '__main__':
    main()
    
