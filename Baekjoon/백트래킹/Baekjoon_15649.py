"""
N과 M (1)
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	88802	56260	36519	62.506%
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
예제 출력 1 
1
2
3
예제 입력 2 
4 2
예제 출력 2 
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
예제 입력 3 
4 4
예제 출력 3 
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1
3 1 2 4
3 1 4 2
3 2 1 4
3 2 4 1
3 4 1 2
3 4 2 1
4 1 2 3
4 1 3 2
4 2 1 3
4 2 3 1
4 3 1 2
4 3 2 1
"""

from itertools import permutations

n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]
res = list(permutations(arr, m))

for i in res: print(*i)



def func(k):  # 현재 k개까지 수를 택했음.
    if k == m:  # m개를 모두 택했으면
        for i in range(m):
            print(arr[i], end=' ')  # arr에 기록해둔 수를 출력
        print()
        return

    for i in range(1, n + 1):  # 1부터 n까지의 수에 대해
        if not visited[i]:  # 아직 i가 사용되지 않았으면
            arr[k] = i  # k번째 수를 i로 정함
            visited[i] = True  # i를 사용되었다고 표시
            func(k + 1)  # 다음 수를 정하러 한 단계 더 들어감
            visited[i] = False  # k번째 수를 i로 정한 모든 경우에 대해 다 확인했으니 i를 이제 사용되지 않았다고 명시함.

n, m = map(int, input().split())
arr = [0] * 10
visited = [False] * 10
func(0)
