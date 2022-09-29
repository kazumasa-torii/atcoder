def main():
    tmp = 'abc'
    s = input()
    n = len(s)
    ans = str()
    for i in range(n):
        if s[i] == '1':ans += '1'
        elif s[i] == '0':ans += '0'
        else: ans = ans[:-1]
    print(ans)
    return

if __name__ == '__main__':
    main()