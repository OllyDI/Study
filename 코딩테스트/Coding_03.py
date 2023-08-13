"""
다음 조건들이 모두 성립되는 경우 짝이 맞는 괄호로 판정 됩니다.

- 문자열 s는 다음과 같은 괄호들로만 구성되어 있습니다. ‘(’ , ‘)’ , ‘{’ , ‘}’ , ‘[’ , ‘]’
- 열린 괄호는 같은 유형 괄호로 닫아야 합니다.
- 여는 괄호는 반드시 올바른 순서로 닫아야 합니다.

문자열 `s`가 주어졌을 때, 문자열 `s`가 짝이 맞는 괄호이면 `true`를, 짝이 맞지 않는 괄호이면 `false`를 return 하는 함수를 작성하시오.
"""

import sys
input = sys.stdin.readline

s = ["(", "[", ")", "]"]

def func(str):
    stack = []      # 스택의 LIFO를 이용
    check = "true"

    for chr in str:
        if chr == "(" or chr == "[": stack.append(chr)
        elif chr == ")" or chr == "]":
            if not stack:
                check = "false"
                break
            else:
                if s[s.index(chr) - 2] == stack[-1]: stack.pop(-1)
                else:
                    check = "false"
                    break
    
    if not stack: return check
    else: return "false"

str = input().rstrip()
print(func(str))