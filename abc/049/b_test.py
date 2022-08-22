from distutils.spawn import spawn
import sys
import time
from io import StringIO

_INPUT = """\
9 20
.....***....***.....
....*...*..*...*....
...*.....**.....*...
...*.....*......*...
....*.....*....*....
.....**..*...**.....
.......*..*.*.......
........**.*........
.........**.........

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    h, w = map(int, input().split())
    maps = []
    for _ in range(h):
        a = input()
        maps.append(a)
        maps.append(a)

    for i in maps:
        print(i)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
