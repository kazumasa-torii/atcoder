from collections import deque
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    q = deque()
    for i in range(n):
        q.append(a[i])

    while len(q) != 1:
        one = q.popleft()
        two = q.popleft()
        q.append((one + two)/2)
    ans = q.pop()
    print(ans)
    return

if __name__ == '__main__':
    main()
