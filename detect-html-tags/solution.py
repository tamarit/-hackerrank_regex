# https://www.hackerrank.com/challenges/detect-html-tags/

import re
    
if __name__ == '__main__':
    total = int(input())
    tags = set()
    for _ in range(total):
        line = input()
        for m in re.finditer(r"(?:\<\s*([A-Za-z\d]+)(?:\s[^\>]*?)?\/?>)", line):
            tags.add(m.group(1))
    print(";".join(sorted(list(tags))))