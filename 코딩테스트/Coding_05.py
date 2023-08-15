"""
경우의 수 찾기 프로그램이 있습니다. n개의 음이 아닌 정수들이 주어지며, 해당 프로그램은 이 정수들의 순서를 바꾸지 않고 적절히 더하거나 
빼는 연산만을 통해 목표 값 target을 만드는 경우의 수를 return 합니다. 예를 들어 [4, 1, 2, 1]로 숫자 4를 만들려면 다음과 같은 경우들을 찾아 경우의 수인 2를 return 하게 됩니다.

+4+1-2+1 = 4
+4-1+2-1 = 4

사용할 수 있는 숫자가 담긴 배열 `numbers`과 찾으려는 값인 정수 `target`이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 목표 값이 나오는 경우의 수를 return하는 함수를 작성하시오.

- 2 ≤ numbers.length ≤ 20
- 1 ≤ numbers[i] ≤ 50
- 1 ≤ target ≤ 1000
"""

def func(numbers, target):
    total = sum(numbers)

    if (total + target) % 2 != 0 or target > total: return 0    # 리스트 합과 타겟을 더했을 때 홀수면 리스트로 타겟 값을 만들 수 없음

    tsum = (total + target) // 2                                # 동적계획법 중 경우의 수만큼 배열 생성
    arr = [0] * (tsum + 1)
    arr[0] = 1

    for num in numbers:
        for j in range(tsum, num - 1, -1):
            arr[j] += arr[j - num]
    return arr[tsum]

numbers = list(map(int, input().split()))
target = int(input())
print(func(numbers, target))
