# https://www.hackerrank.com/challenges/split-number

import re
    
if __name__ == '__main__':
    total = int(input())
    for _ in range(total):
        number = input().strip()
        m = re.search(r"^(\d{1,3})[\- ](\d+)[\- ](\d{4,10})$", number)
        print(f"CountryCode={m.group(1)},LocalAreaCode={m.group(2)},Number={m.group(3)}")