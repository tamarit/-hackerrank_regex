# https://www.hackerrank.com/challenges/find-hackerrank

import re
    
if __name__ == '__main__':
    total = int(input())
    for _ in range(total):
        line = input().strip()
        start = False
        end = False
        for m in re.finditer(r"hackerrank", line):
            if m.start() == 0:
                start = True
            if m.end() == len(line):
                end = True
        if start and end:
            print(0)
        elif start:
            print(1)
        elif end:
            print(2)
        else:
            print(-1)
