"""
소가 길을 건너간 이유 5 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	4475	2145	1760	46.610%
문제
농부 존의 농장에 원형 길이 있다고 했지만, 길은 그뿐만이 아니다. 그 옆에 일자형 길이 있는데, 1번부터 N번까지의 번호가 붙은 횡단보도 N (1 ≤ N ≤ 100,000)개로 이루어져 있다. 

교통사고를 방지하기 위해 존은 각 횡단보도에 신호등을 설치해 놓았다. 그러던 어느 날, 강력한 뇌우로 인해 몇몇 신호등이 망가졌다. 존은 연속한 K개의 신호등이 존재하도록 신호등을 수리하고 싶다. 이번에도 우리가 존을 도와주자.

입력
첫 줄에 N, K, B (1 ≤ B,K ≤ N)가 주어진다. 그 다음 B줄에는 고장난 신호등의 번호가 하나씩 주어진다.

출력
정상적으로 작동하는 연속 K개의 신호등이 존재하려면 최소 몇 개의 신호등을 수리해야 하는지 출력한다.

예제 입력 1 
10 6 5
2
10
1
5
9
예제 출력 1 
1
"""

# 슬라이딩 윈도우 알고리즘
import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
traffic = list(i + 1 for i in range(n))

for i in range(b): traffic[int(input()) - 1] = -1

res = 0
for i in range(k): 
    if traffic[i] == -1: res += 1

cnt = res
for i in range(1, n - k + 1):
    if traffic[i - 1] == -1: cnt -= 1
    if traffic[i + k - 1] == -1: cnt += 1
    res = min(res, cnt)

print(res)