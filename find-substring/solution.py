# https://www.hackerrank.com/challenges/find-substring/

import re
    
if __name__ == '__main__':
    total = int(input())
    sentences = []
    for _ in range(total):
        sentences.append(input())
    total = int(input())
    queries = []
    for _ in range(total):
        queries.append(input())
    for q in queries:
        escaped_q = re.escape(q)
        total_found = 0
        for s in sentences:
            total_found += len(re.findall(r"\w" + escaped_q + r"\w", s))
        print(total_found)