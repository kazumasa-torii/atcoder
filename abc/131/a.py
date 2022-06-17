def main():
    S = input()
    flag = True
    if S[0] == S[1]:
        flag = False
    elif S[1] == S[2]:
        flag = False
    elif S[2] == S[3]:
        flag = False
    
    print('Good' if flag else 'Bad')

    return

main()
