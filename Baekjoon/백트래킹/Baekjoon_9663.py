"""
N-Queen
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
10 초	128 MB	95075	45612	29611	46.723%
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1 
8
예제 출력 1 
92
"""

def dfs(cnt) :
    global val
    
    if cnt >= n : val += 1
    else :
        for i in range(n) :
            lst[cnt] = i
            b = True

            for j in range(cnt):
                if lst[cnt] == lst[j] or abs(lst[cnt] - lst[j]) == cnt - j:
                    b = False
                    break
            
            if b: dfs(cnt + 1)

n = int(input())
lst = [0 for _ in range(n)]
val = 0

dfs(0)
print(val)