"""
그대로 출력하기
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	271234	88458	73814	34.977%
문제
입력 받은 대로 출력하는 프로그램을 작성하시오.

입력
입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.

출력
입력받은 그대로 출력한다.

예제 입력 1 
Hello
Baekjoon
Online Judge
예제 출력 1 
Hello
Baekjoon
Online Judge
"""

# import sys
# input = sys.stdin.readline
# 해당 문제는 입력의 종료 조건이 없어서 input()의 아무 입력이 없으면 EOFError 처리를 해 종료 시켜 줘야 됨
# 위의 sys를 쓰게 되면 아무 입력이 없을 때 EOFError가 아닌 공백을 출력하기 때문에 sys를 쓰면 에러가 발생


while True: 
    try:
        print(input())
    except EOFError: break
