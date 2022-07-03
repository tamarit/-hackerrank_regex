# https://www.hackerrank.com/challenges/detect-the-domain-name

import re
    
if __name__ == '__main__':
    total = int(input())
    sentences = []
    for _ in range(total):
        sentences.append(input().strip())
    domains = set()
    for s in sentences:
        for m in re.finditer(r"https?\:\/\/(?:(?:www|ww2).)?([a-zA-Z\d\-]*\.(?:[a-zA-Z\d\-\.]+))(?:[^a-zA-Z\d\.])", s):
            # print(m)
            domains.add(m.group(1))
    print(";".join(sorted(domains)))