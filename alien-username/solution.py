# https://www.hackerrank.com/challenges/alien-username

import re
    
if __name__ == '__main__':
    total = int(input())
    sentences = []
    for _ in range(total):
        sentences.append(input())
    for s in sentences:
        if re.search(r"^[\_\.]\d+[A-Za-z]*\_?$", s) is None:
            print("INVALID")
        else:
            print("VALID")