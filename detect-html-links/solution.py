# https://www.hackerrank.com/challenges/detect-html-links/

import re
    
if __name__ == '__main__':
    total = int(input())
    for _ in range(total):
        line = input()
        for m in re.finditer(r"(?:\<a\s+.*?href\=\"(.*?)\".*?\>(.*?)\<\s*\/\s*a\s*\>)|(?:\<a\s+.*?href\=\"(.*?)\".*?(.*?)\s*\/\s*\>)", line):
            try:
                url_str = m.group(1).strip()
                name = m.group(2).strip()
            except:
                url_str = m.group(3).strip()
                name = m.group(4).strip()
            while name.startswith("<"):
                # print(url_str)
                # print(name)
                m_name = re.search(r"(?:\<(.*?)(?:\s.*?)?\>(.*?)\<\/\1\>)|(?:\<(.*?)\s.*?\/\>)", name)
                try:
                    name = m_name.group(2).strip()
                except:
                    name = ""
            print(f"{url_str},{name}")
