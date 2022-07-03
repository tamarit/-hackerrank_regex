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
    ids = []
    for m in re.finditer(r"id\s*\=\s*\"question\-summary\-(\d+)\"", code.strip()):
        ids.append(m.group(1).strip())
    questions = []
    for m in re.finditer(r"\<\s*h3\s*\>\s*\<\s*a\s*href\s*\=\s*\"\/questions\/\d+/.*?\"\s*class\s*=\s*\"question-hyperlink\"\s*\>(.*?)\<\s*\/\s*a\s*\>\s*\<\s*\/\s*h3\s*\>", code.strip()):
        questions.append(m.group(1).strip())
    times_asked = []
    for m in re.finditer(r"asked\s*\<\s*span\s*title\s*\=\s*\".+?\"\s*class\s*\=\s*\"relativetime\"\>(.*?)\<\s*\/\s*span\s*\>",  code.strip()):
        times_asked.append(m.group(1).strip())
    for id, question, time_asked in zip(ids, questions, times_asked):
        print(";".join([id, question, time_asked]))
    # print(ids)
    # print(questions)
    # print(times_asked)
