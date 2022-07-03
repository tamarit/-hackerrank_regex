# https://www.hackerrank.com/challenges/programming-language-detection

import re
    
if __name__ == '__main__':
    has_content = True
    code = ""
    while has_content:
        try:
            code += input().strip() + "\n"
        except EOFError:
            has_content = False
    if re.search(r"class\s+.{,30}\{", code.strip(), re.DOTALL):
        print("Java")
    elif re.search(r"def\s+.+\:", code.strip()):
        print("Python")
    elif re.search(r"print\s+.*", code.strip()):
        print("Python")
    else:
        print("C")