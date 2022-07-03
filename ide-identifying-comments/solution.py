# https://www.hackerrank.com/challenges/ide-identifying-comments

import re
    
if __name__ == '__main__':
    has_content = True
    code = ""
    while has_content:
        try:
            code += input().strip() + "\n"
        except EOFError:
            has_content = False
    for s in re.findall(r"(?:\/\/.*?(?=\n))|(?:\/\*.*?\*\/)", code.strip(), re.DOTALL):
        print(s)