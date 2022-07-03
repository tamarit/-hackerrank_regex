# https://www.hackerrank.com/challenges/ip-address-validation

import re
    
if __name__ == '__main__':
    total = int(input())
    sentences = []
    for _ in range(total):
        sentences.append(input())
    for s in sentences:
        s = s.strip()
        pattern_ipv4 = r"((25[0-5])|(2[0-4]\d)|(1?\d?\d))"
        pattern_ipv4_full = r"^(" + pattern_ipv4 + r"\.){3}" + pattern_ipv4 + r"$"
        # print(pattern_ipv4_full)
        if re.search(pattern_ipv4_full, s) is not None:
            print("IPv4")
        else:
            pattern_ipv8_single = r"[A-Fa-f\d]"
            pattern_ipv8 = r"((" + pattern_ipv8_single + r"?){3}" + pattern_ipv8_single + r")"
            pattern_ipv8_full = r"^(" + pattern_ipv8 + r"\:){7}" + pattern_ipv8 + r"$"
            # print(pattern_ipv8_full)
            if re.search(pattern_ipv8_full, s) is not None:
                print("IPv6")
            else:
                print("Neither")