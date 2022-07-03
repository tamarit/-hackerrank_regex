# https://www.hackerrank.com/challenges/utopian-identification-number

import re
    
if __name__ == '__main__':
    total = int(input())
    for _ in range(total):
        number = input().strip()
        if re.search(r"^[a-z]{0,3}\d{2,8}[A-Z]{3,}$", number) is not None:
            print("VALID")
        else:
            print("INVALID")