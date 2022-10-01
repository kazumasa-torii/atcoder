def main():
    nums = [0, 0, 0]
    s = list(input())
    for i in s:
        if i == 'a':nums[0] += 1 
        if i == 'b':nums[1] += 1 
        if i == 'c':nums[2] += 1
    print('YES' if max(nums) - min(nums) <= 1 else 'NO') 
    return

if __name__ == '__main__':
    main()