# https://www.hackerrank.com/challenges/hackerrank-tweets

import re
    
if __name__ == '__main__':
    total = int(input())
    sentences = []
    for _ in range(total):
        sentences.append(input().strip())
    count = 0
    for s in sentences:
        if re.search(r"[\#\@]?[Hh][Aa][cC][kK][eE][rR][rR][aA][nN][kK]", s):
            count += 1
    print(count)