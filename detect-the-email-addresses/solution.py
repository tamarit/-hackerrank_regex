# https://www.hackerrank.com/challenges/detect-the-email-addresses

import re
    
if __name__ == '__main__':
    total = int(input())
    sentences = []
    for _ in range(total):
        sentences.append(input())
    # addresses = []
    email_part = r"(?:\w+\.?)*\w+"
    email_full = email_part + r"\@" + email_part
    email_full = r"(?:[\w\.]+\w)\@(?:[\w\.]+\w)"
    # print(email_full)
    # for s in sentences:
    #     # print(email_full)
    #     addresses += re.findall(email_full, s)
    addresses = re.findall(email_full, " ".join(sentences))
    # print(sorted(list(addresses)))
    print(";".join(sorted(set(addresses))))