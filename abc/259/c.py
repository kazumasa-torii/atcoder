"""

"""
import sys
input = sys.stdin.readline
def main():
    def rle(s):
        li = []
        for c in range(len(s)):
            if c == 0:
                li.append([s[c], 1])
            elif len(s) > 0 and li[-1][0] == s[c]:
                li[-1][1] += 1
            else:
                li.append([s[c], 1])
        return li

    def solve(a, b):
        # 文字の種類の並びが同じじゃないと False
        if len(a) != len(b): return False
        for i in range(len(a)):
            # 文字種類が同じじゃないと False
            if a[i][0] != b[i][0]: return False
            al = a[i][1]
            bl = b[i][1]
            # 文字が同じで重なりが1つだけの場合
            if al == 1:
                # bの文字列が一つじゃない場合は False
                if bl != 1: return False
                else:
                    # aよりbが小さい場合は、False
                    if bl < al: return False
        return True

    S = input()
    T = input()
    s_list = rle(S)
    t_list = rle(T)
    print('Yes' if solve(s_list, t_list) else 'No')

    return

main()
