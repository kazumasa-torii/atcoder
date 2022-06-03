"""
for一つで考える
"""
import sys
import re
input = sys.stdin.readline
S = input().split()
S = S[0]
if re.search('[A-Z]', S) and re.search('[a-z]', S) and len(set(S)) == len(S):
    print('Yes')
else:
    print('No')
