import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
100

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)


import datetime
def main():
    K = int(input())
    dt = datetime.datetime(2022, 7, 2, 21, 0)
    dt = dt + datetime.timedelta(minutes=K)
    ho = str(dt.hour)
    mi = str(dt.minute)
    if len(ho) == 1:
        ho = '0' + str(ho)
    if len(mi) == 1:
        mi = '0' + str(mi)
    print(f'{str(ho)}:{str(mi)}')
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
