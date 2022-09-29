import string
def main():
    s = input()
    ret = 100000000000000
    for c in string.ascii_lowercase:
        if c not in s:
            continue;
        x = s.split(c)
        m = 0
        for ss in x:
            m = max(m, len(ss))
        ret = min(ret, m)
    print(ret)
    return

if __name__ == '__main__':
    main()