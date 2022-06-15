def main():
    num = int(input())
    flag = True
    if num == 1: return False
    for i in range(2, num+1):
        if i * i > num:
            break
        if num % i == 0:
            flag = False
    return flag

if __name__ == '__main__':
    print('Yes' if main() else 'No')
