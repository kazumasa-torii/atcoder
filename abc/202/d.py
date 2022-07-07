import sys
input = sys.stdin.readline

def main():
    A, B, K = map(int, input().split())
    pascal = [[1]]
    for i in range(1,A+B+1):
        tmp = [1]
        if i > 1:
            for j in range(1,i):
                tmp.append(pascal[i-1][j-1]+pascal[i-1][j])
        tmp.append(1)
        pascal.append(tmp)
    ans = str()
    while A+B > 0:
        x = 0
        if A >= 1: x = pascal[A+B-1][A-1]
        if K <= x:
            ans += 'a'
            A -= 1
        else:
            ans += 'b'
            B -= 1
            K -=x
    print(ans)

    return

main()
