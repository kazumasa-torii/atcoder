"""
1.連続している数記載する、ただしその時は1-0-1-0-1-0-1-0-1のように1で始まりと終わりが終わっている状態で記載していく
1.累積和を作る
1.区間で1からK個の0の連続した数を含めた1の終端までの距離を求める
1.区間から求めた数の最終的な数が大きいサイズのものを答える

この回答肝は累積和の作る前の考え方
最初の配列の作り方を理解しておかないとだめ
"""
def main():
    N, K = map(int,input().split())
    S = input()
    Nums = []
    now = 1
    cnt = 0

    # 0と1の連続している数を記載
    for i in range(N):
        if S[i] == str(now):
            cnt += 1
        else:
            Nums.append(cnt)
            now = 1 - now
            cnt = 1

    # 終わりの数はappendされないので記載する
    if cnt != 0:
        Nums.append(cnt)

    if len(Nums) % 2 == 0:
        Nums.append(0)

    Csum = [0] * (len(Nums) + 1)
    for i in range(len(Nums)):
        Csum[i+1] = Csum[i] + Nums[i]

    Add = 2 * K + 1
    ans = 0

    # 1からスタートなので偶数目のみ見て全体の距離を求める
    for i in range(0, len(Nums), 2):
        tmp = 0
        left = i
        right = min(i+Add, len(Nums))
        tmp = Csum[right] - Csum[left]
        ans = max(tmp, ans)

    print(ans)

main()
