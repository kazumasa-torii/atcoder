def main():
    s = input()
    divide = ['dream', 'erase','dreamer', 'eraser']

    s = s[::-1]
    for i in range(4):
        divide[i] = divide[i][::-1]
    
    can = True
    n = len(s)
    idx = 0
    while idx < n:
        can2 = False
        for j in range(4):
            d = divide[j]
            dlen = len(d)
            if s[idx:idx+dlen] == d:
                can2 = True
                idx += dlen
        if not can2:
            can = False
            break
    
    print('YES' if can else 'NO')
    return

if __name__ == '__main__':
    main()
