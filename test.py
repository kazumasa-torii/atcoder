import sys
import time
from io import StringIO

_INPUT = """\
((())
"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def solution(s):
        brackets = ["(","[","{"]
        bracketsList = []
        resultFlag = True
        for bracket in list(s):
            if bracket in brackets:
                bracketsList.append(bracket)
                continue
            if bracket == ")":
                fit = bracketsList.pop()
                if fit != "(": resultFlag = False
            elif bracket == "]":
                fit = bracketsList.pop()
                if fit != "[": resultFlag = False
            elif bracket == "}":
                fit = bracketsList.pop()
                if fit != "{": resultFlag = False
        if len(bracketsList) > 0: resultFlag = False
        return resultFlag
    s = input()
    print(solution(s))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
