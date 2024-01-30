"""

"""

def min_presses_to_red(n, k, bulbs):
    current_state = list(bulbs)
    rules = {'R': 'G', 'G': 'B', 'B': 'R'}
    presses = 0

    for i in range(n - k + 1):
        if current_state[i] != 'R':
            presses += 1
            for j in range(k):
                current_state[i + j] = rules[current_state[i + j]]

    return presses

# 예시
n = 6
k = 3
bulbs = "GBBRGB"
result = min_presses_to_red(n, k, bulbs)
print(result)