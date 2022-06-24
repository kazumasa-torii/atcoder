"""
最終的にRLのところに収束するのでそこまでのRとLのグループを数え上げて対応する
収束するまではわかったがどのように計算するべきか理解できていないのでそこが問題

1. 左からRを数え上げて行きLにぶつかればそこで数え上げた個数が偶数、奇数で切り分ける
1. 個数が奇数の場合は、R側は偶数になるので数え上げた個数を2で割って切り捨てる
1. 個数が偶数の場合は、R側は奇数になるので偶数で計算した数字から引いた数を割り当てる
1. 上記の内容を左からLを数え上げていき同じ内容でおこなう
"""

def main():
    S = input()
    N = len(S)

    ans = [0]*N  # 最終的に出力する答え（10**100操作後に、各iに人がいる人数）

    # Rグループについて考える
    cnt = 0  # 現在のRグループの人数
    for i, moji in enumerate(S):
        if moji == "R":
            cnt += 1
            continue
        else:
            even_num = cnt//2         # 折返し地点までの距離が偶数の人の数
            odd_num = cnt - even_num  # 折返し地点までの距離が奇数の人の数
            ans[i] += even_num        # 折返し地点までの距離が偶数の人は、ans[i]に収束する
            ans[i-1] += odd_num       # 折返し地点までの距離が奇数の人は、ans[i-1]に収束する
            cnt = 0

    # Lグループについて考える
    cnt = 0  # Lグループの人数
    for i in range(N-1, -1, -1):
        if S[i] == "L":
            cnt += 1
            continue
        else:
            even_num = cnt//2
            odd_num = cnt - even_num
            ans[i] += even_num
            ans[i+1] += odd_num
            cnt = 0

    print(*ans)


if __name__ == "__main__":
    main()
