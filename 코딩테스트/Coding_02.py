"""
2번
단어나 문장의 문자 순서를 바꾸어 다른 단어나 문장을 만드는 것을 “아나그램”이라고 합니다. 문자열 `s`가 주어졌을 때 
`t`가 `s`의 아나그램이면 `true`를, 그렇지 않으면 `false`를 return하는 함수를 작성하시오.

- t와 s는 모두 소문자로 되어있는 문자열입니다.
- 1 ≤ s.length, t.length ≤ 5 * 10⁴
입출력 예시
s hot t toh answer true
"""

def anagram(s, t):
    res = "true"
    for i in range(len(s)):
        if s[i] != t[-1 - i]:   #s의 처음과 t끝 비교검사
            res = "false"
            return res
    return res

s = input()
t = input()
print(anagram(s, t))