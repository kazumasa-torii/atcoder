def main():
    ans = "keyence"
    s = list(input())
    n = len(ans)
    for i in range(n):
        while len(s) > 0:
            if ans[i] == s[i]:break
            del s[i]
    s = ''.join(s)
    print('YES' if ans == s else 'NO')

    return

if __name__ == '__main__':
    main()