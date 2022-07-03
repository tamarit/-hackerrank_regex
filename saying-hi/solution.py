# https://www.hackerrank.com/challenges/saying-hi

import re
    
if __name__ == '__main__':
    total = int(input())
    for _ in range(total):
        line = input().strip()
        if re.search(r"^[Hh][Ii]\s[^Dd]", line):
            print(line)
