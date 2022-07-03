# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude

import re
    
if __name__ == '__main__':
    total = int(input())
    sentences = []
    for _ in range(total):
        sentences.append(input().strip())
    for s in sentences:
        number_regex = r"([\-\+]?\d+(?:\.\d+)?)"
        full_regex = r"^\(" + number_regex + r"\,\s" + number_regex + r"\)$"
        # print(full_regex)
        m = re.search(full_regex, s)
        if m is None:
            print("Invalid")
        else:
            valid = True
            for i, limit in [(1, 90), (2, 180)]:
                value = float(m.group(i))
                clean_number = re.sub(r"[\+\-]", "", m.group(i))
                # print(clean_number)
                # print(value)
                if not (-limit <= value <= limit and (value == 0 or not clean_number.startswith("0"))):
                    valid = False
                    break
            if valid:
                print("Valid")
            else:
                print("Invalid")