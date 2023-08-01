"""
정수로 이루어진 `nums`가 주어졌을 때 목표 숫자인 `target`이 존재하면 target이 존재하는 곳의 인덱스를, 존재하지 않는다면 -1을 반환하는 프로그램을 작성하시오.

- 1 ≤ nums.length ≤ 10⁴
- -10⁴ < nums[i], target < 10⁴
- nums의 모든 숫자는 고유합니다.
- nums는 오름차순으로 정렬되어 있습니다.

입출력 예시

입력: nums = [-1, 0, 3, 5, 9, 12], target = 9
출력: 4
설명: nums에는 9가 존재하고 인덱스는 4입니다.

입력: nums = [-1, 0, 3, 5, 9, 12], target = 2
출력: -1
설명: nums에는 2가 없으므로 -1을 반환합니다.
"""

def check(nums, target):
    if target in nums: return nums.index(target)
    else: return -1

nums = list(map(int, input().split()))
target = int(input())

print(check(nums, target))