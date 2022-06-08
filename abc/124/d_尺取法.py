"""
1.連続している数記載する、ただしその時は1-0-1-0-1-0-1-0-1のように1で始まりと終わりが終わっている状態で記載していく
1.
1.
1.

"""
def main():
    # N, K = map(int,input().split())
    # S = input()
    N, K = 14, 2
    S = '11101010110011'

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

    # 1-0-1-0-1-0-1 って感じの配列が欲しい
    # 1-0-1-0-1-0 みたいに0で終わっていたら適当に1つ足す
    if len(Nums) % 2 == 0:
        Nums.append(0)

    print(Nums)
    Add = 2 * K + 1
    ans = 0

    left = 0
    right = 0
    tmp = 0
    # 1からスタートなので偶数目の0を変えたら全体の距離を求める
    for i in range(0, len(Nums), 2):
        # 次のleft と rigthを計算
        Nextleft = i
        Nextright = min(i + Add, len(Nums))
        print(f"{i}番目 , NextLeft : {Nextleft}, Nextright : {Nextright}")
        while Nextleft > left:
            print(f"left : {left},  tmp : {tmp}, Nums : {Nums[left]}")
            tmp -= Nums[left]
            left += 1

        while Nextright > right:
            print(f"right : {right},  tmp : {tmp}, Nums : {Nums[right]}")
            tmp += Nums[right]
            right +=1

        ans = max(tmp, ans)
    # print(ans)

main()
