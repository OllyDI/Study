"""
팰린드롬 만들기
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	34711	15276	11318	43.202%
문제
임한수와 임문빈은 서로 사랑하는 사이이다.

임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.

임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

입력
첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.

출력
첫째 줄에 문제의 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다. 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.

예제 입력 1 
AABB
예제 출력 1 
ABBA
예제 입력 2 
AAABB
예제 출력 2 
ABABA
예제 입력 3 
ABACABA
예제 출력 3 
AABCBAA
예제 입력 4 
ABCD
예제 출력 4 
I'm Sorry Hansoo
"""

# 난이도에 비해 까다로운 문제

import sys
import collections
input = sys.stdin.readline

al = input().rstrip()
cword = sorted((collections.Counter(al)).items())
res = ''
mid = ''
check = 0

for al, cnt in cword:
    if cnt % 2: 
        check += 1
        mid = al
    res += al * (cnt // 2)

if check > 1: print("I'm Sorry Hansoo")
else:
    if check: res += mid + res[::-1]
    else: res += res[::-1]

    print(res)