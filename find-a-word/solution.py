# https://www.hackerrank.com/challenges/find-a-word
import re
from collections import Counter
    
if __name__ == '__main__':
    total = int(input())
    sentences = []
    for _ in range(total):
        sentences.append(input().strip())
    total_queries = int(input())
    queries = []
    for _ in range(total_queries):
        queries.append(input().strip())
    word_counter = Counter()
    for s in sentences:
        word_counter.update(re.findall("\w+",s))
    for q in queries:
        print(word_counter[q])