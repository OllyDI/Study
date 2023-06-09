n = int(input())
lst = [0 for _ in range(16)]
val = 0

def dfs(cnt) :
    global val
    if cnt > n : val += 1
    else :
        for i in range(1, n + 1) :
            lst[cnt] = i
            boolean = True

            for j in range(1, cnt):
                if lst[cnt] == lst[j] or abs(lst[cnt] - lst[j]) == cnt - j:
                    boolean = False
                    break
            
            if boolean : dfs(cnt + 1)

dfs(1)
print(val)