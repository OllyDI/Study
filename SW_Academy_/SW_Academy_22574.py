"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AZIieDaq5AEDFAXd&categoryId=AZIieDaq5AEDFAXd&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
22574. 높은 곳으로 D3

 
Master

 pr0ved
1,761
참여자
2,030
제출
642
정답
31.63
정답률
100
Point
Problem제출이력정답
시간 : 72개 테스트케이스를 합쳐서 C의 경우 1초 / C++의 경우 1초 / Java의 경우 2초 / Python의 경우 3초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

 

0층부터 109층까지, 총 109+1개의 층으로 구성된 건물이 있다. 처음에 엘리베이터는 0층에 멈춰 있다.

당신은 건물 안에 있는 엘리베이터를 타고 가장 높은 층으로 가고자 한다.

 

엘리베이터의 버튼은 건물의 관리인만이 누를 수 있다. 관리인은 당신에게 총 N번의 선택의 기회를 준다.

이 중 i (1 ≤ i ≤ N)번째 선택에서, 당신은 엘리베이터를 가만히 놔 둘 지, 아니면 위로 i층을 올릴지 정할 수 있다.

당신의 선택에 따라, 원래 엘리베이터가 x층에 있었다면, i번째 선택 이후에는 엘리베이터가 계속 x층에 머물러 있을 수도 있고,

위로 이동하여 x+i층에 멈출 수도 있다.

 

건물의 P층에는 폭탄이 설치되어 있다. 당신의 선택에 의해 엘리베이터가 P층에 멈춘다면 그 순간 폭탄이 터지게 될 것이므로,

P층에 도착하지 않도록 모든 순간에 적절히 선택을 해야 한다. P ≠ 0 이므로, 시작부터 폭탄이 터지는 일은 없다.

 

이러한 상황에서, 모든 N번의 선택이 끝났을 때 당신이 있을 수 있는 가장 높은 층의 번호를 구하는 프로그램을 작성하라.

 

 
[입력] 

 

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스는 하나의 줄로 이루어지며, 두 개의 정수 N (1 ≤ N ≤ 2,000)과 P (1 ≤ P ≤ 4,000,000)가 공백 하나를 사이로 두고 주어진다.

 

 

[출력]
각 테스트 케이스마다, 엘리베이터가 P층에 멈추지 않았을 때 도착할 수 있는 가장 높은 층 번호를 한 줄에 하나씩 출력한다.

 
입력
3
2 2
2 1
10 10000

출력
3
2
55
"""

T = int(input())

for test_case in range(1, T + 1):
    n, p = map(int, input().split())

    floor = 0

    for i in range(1, n + 1):
        if floor + i == p: floor += i - 1
        else: floor += i
    print(floor)