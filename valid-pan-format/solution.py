# https://www.hackerrank.com/challenges/valid-pan-format

import re
    
if __name__ == '__main__':
    total = int(input())
    for _ in range(total):
        number = input().strip()
        # <char><char><char><char><char><digit><digit><digit><digit><char>
        if re.search(r"^[A-Z]{5}\d{4}[A-Z]$", number) is not None:
            print("YES")
        else:
            print("NO")