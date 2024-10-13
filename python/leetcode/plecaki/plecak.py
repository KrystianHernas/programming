MAX_N, MAX_M = 1000, 10000
visited = [[-1] * (MAX_M + 1) for i in range(MAX_N + 1)]
def plecakiMaxValue(N, M, weights, values):
    res1 = -1
    res2 = -1

    if N ==-1:
        return 0
    if visited[N][M] != -1:
        print(f"N:{N} M:{M} visited:{visited[N][M]}")
        return visited[N][M]

    if M >= weights[N-1]:
        res1 = values[N-1] + plecakiMaxValue(N, M - weights[N-1], weights, values)
    # 2. Idę dalej
    res2 = plecakiMaxValue(N-1, M, weights, values)
    visited[N][M] = max(res1, res2)
    print(f"N:{N} M:{M} visited:{visited[N][M]}")
    return visited[N][M]

# N, M = 3, 3
# weights = [1,2,3]
# values =  [2,2,2]
N, M = 10, 20
weights = [8, 3, 4, 2, 4, 7, 4, 1, 2, 3]
values = [3, 8, 1, 3, 3, 6, 3, 1, 2, 3]
max_value = plecakiMaxValue(N, M, weights, values)
print(f"Maximum value: {max_value}")