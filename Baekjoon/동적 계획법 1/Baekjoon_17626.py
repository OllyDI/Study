"""
Four Squares 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초 (추가 시간 없음)	512 MB	36338	15998	12597	43.761%
문제
라그랑주는 1770년에 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명하였다. 어떤 자연수는 복수의 방법으로 표현된다. 예를 들면, 26은 52과 12의 합이다; 또한 42 + 32 + 12으로 표현할 수도 있다. 역사적으로 암산의 명수들에게 공통적으로 주어지는 문제가 바로 자연수를 넷 혹은 그 이하의 제곱수 합으로 나타내라는 것이었다. 1900년대 초반에 한 암산가가 15663 = 1252 + 62 + 12 + 12라는 해를 구하는데 8초가 걸렸다는 보고가 있다. 좀 더 어려운 문제에 대해서는 56초가 걸렸다: 11339 = 1052 + 152 + 82 + 52.

자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램을 작성하시오.

입력
입력은 표준입력을 사용한다. 입력은 자연수 n을 포함하는 한 줄로 구성된다. 여기서, 1 ≤ n ≤ 50,000이다.

출력
출력은 표준출력을 사용한다. 합이 n과 같게 되는 제곱수들의 최소 개수를 한 줄에 출력한다.

예제 입력 1 
25
예제 출력 1 
1
예제 입력 2 
26
예제 출력 2 
2
예제 입력 3 
11339
예제 출력 3 
3
예제 입력 4 
34567
예제 출력 4 
4
"""

# 해설을 봐도 이해가 안되는 문제 **다시보기**

import math
import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n + 1): # 0, 1 제외 + N까지 봐야되기 때문에  -> 2 ~ n + 1
    minVal = 1e9

    for j in range(1, int(math.sqrt(i)) + 1):
        minVal = min(minVal, dp[i - j**2])
    dp.append(minVal + 1)
print(dp[n])