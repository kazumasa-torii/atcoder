def main():
    N = input()
    one = '0'
    two = '1'
    if len(N) == 0:
        print(0)
        return

    for _ in range(len(N)-1):
        if one[-1] == '1': one += '0'
        else: one += '1'
        if two[-1] == '1': two += '0'
        else: two += '1'

    one_diff = 0
    two_diff = 0
    for i in range(len(N)):
        if one[i] != N[i]:
            one_diff += 1
        if two[i] != N[i]:
            two_diff += 1

    print(min(one_diff, two_diff))

main()
