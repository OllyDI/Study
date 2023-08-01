"""
1번
정수 `x`가 주어졌을 때 회문이면 `true` 그렇지 않으면 `false`를 리턴하는 함수를 작성하시오. 회문이란, 왼쪽부터 오른쪽으로 읽었을 때, 오른쪽부터 왼쪽으로 읽었을 때가 같은 경우를 뜻합니다.

입출력 예시
입력 : x = 121
출력 : true
설명 : 121은 왼쪽에서 오른쪽으로 읽어도, 오른쪽에서 왼쪽으로 읽어도 121입니다.

입력 : x = -121
출력 : false
설명 : 왼쪽에서 오른쪽은 -121, 오른쪽에서 왼쪽으로는 121입니다.
"""

def pali(n):
    res = "true"
    if n < 0: return "false"    #숫자가 음수면 무조건 False
    else:
        arr = list(map(int, str(n)))
        
        for i in range(len(arr) // 2): 
            if arr[i] != arr[-1 - i]: res = "false"
    return res

n = int(input())
print(pali(n))