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

# from itertools import permutations

# n, m = map(int, input().split())
# arr = [i + 1 for i in range(n)]
# res = list(permutations(arr, m))

# for i in res: print(*i)


def func(depth):
    if depth == m:
        print(*arr, end=' ')
        print()
        return
    
    for i in range(n):
        if visited[i] == False:
            arr.append(i + 1)
            visited[i] = True
            func(depth + 1)
            arr.pop()
            visited[i] = False


n, m = map(int, input().split())
arr = []
visited = [False] * n
func(0)