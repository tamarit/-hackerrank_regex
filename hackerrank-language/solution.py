# https://www.hackerrank.com/challenges/hackerrank-language

import re
    

LANGUAGES_STR = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC"
LANGUAGES = LANGUAGES_STR.split(":")

if __name__ == '__main__':
    total = int(input())
    for _ in range(total):
        line = input().strip()
        m = re.search(r"^\d+\s+([A-Z]+)$", line)
        if m is not None and m.group(1) in LANGUAGES:
            print("VALID")
        else:
            print("INVALID")
