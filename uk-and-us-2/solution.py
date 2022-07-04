# https://www.hackerrank.com/challenges/uk-and-us-2

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
        escaped_q_ame = re.escape(q)
        m_our = re.search("^(.+)our(.*)$", q)
        if m_our is not None:
            escaped_q_bri = re.escape(f"{m_our.group(1)}or{m_our.group(2)}")
        else:
            escaped_q_bri = None
        total_found = 0
        for s in sentences:
            total_found += len(re.findall(r"\b" + escaped_q_ame + r"\b", s)) + (len(re.findall(r"\b" + escaped_q_bri + r"\b", s)) if escaped_q_bri is not None else 0)
        print(total_found)