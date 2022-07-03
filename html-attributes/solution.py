# https://www.hackerrank.com/challenges/html-attributes

import re
    
if __name__ == '__main__':
    total = int(input())
    tags = dict()
    for _ in range(total):
        line = input().strip()
        tag_regex = r"\<\s*([a-z\d]+)\s*([^\>]*)\>"
        attribute_regex = r"([a-z]+)\s*\=([\"\'])[^\2]*?\2"
        for m in re.finditer(tag_regex, line):
            tag = m.group(1)
            content = m.group(2)
            if tag not in tags:
                tags[tag] = set()
            for m1 in re.finditer(attribute_regex, content):
                tags[tag].add(m1.group(1))
    for tag in sorted(tags):
        print(f"{tag}:{','.join(sorted(tags[tag]))}")