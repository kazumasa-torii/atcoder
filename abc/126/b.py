# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

def main():
    a = input()
    m = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    if a[:2] in m and a[2:] in m:
        print('AMBIGUOUS')
    elif a[:2] not in m and a[2:] in m:
        print('YYMM')
    elif a[:2] in m and a[2:] not in m:
        print('MMYY')
    else:
        print('NA')

main()
