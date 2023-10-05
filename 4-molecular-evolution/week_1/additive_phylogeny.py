from limb_length import LimbLength

def AttachmentPoint(matrix: list[list[int]], j):
    for i in range(len(matrix)):
        for k in range(len(matrix)):
            if matrix[i][k] == matrix[i][j]+matrix[k][j]:
                return i, k, matrix[i][k]
    return -1, -1, 0

def AdaptivePhylogeny(matrix: list[list[int]]) -> dict[int, dict[int, int]]:
    n = len(matrix)
    if n == 2:
        return {
            0: {1: matrix[0][1]},
            1: {0: matrix[1][0]},
        }
    limb_len = LimbLength(matrix, n-1, n)
    for i in range(n):
        matrix[i][n-1] -= limb_len
        matrix[n-1][i] -= limb_len
    i, k, len_i_k = AttachmentPoint(matrix, n-1)
    x = matrix[i][n-1]
    print("Limb length for ", n, limb_len)
    matrix = [row[:-1] for row in matrix[:-1]]
    adj = AdaptivePhylogeny(matrix)
    v = GetOrCreateNodeV(adj, i, k, len_i_k, x, n)
    AddJToV(adj, v, n-1, limb_len)
    return adj


def GetOrCreateNodeV(adj: dict[int, dict[int, int]], i: int, k: int, len_i_k: int, x: int, n: int) -> bool:
    v_exists = k not in adj[i]
    print("V exists")

    v = max(max(adj.keys()) + 1, len(matrix))
    if v in adj[i] or v in adj[k]:
        return v
    
    # else create new limb v (between i and k)
    adj[v] = {}
    if x < len_i_k:
        if k in adj[i]:
            del adj[i][k]
            del adj[k][i]
        adj[i][v] = x
        adj[v][i] = x
        adj[v][k] = len_i_k - x
    else:
        adj[k][v] = len_i_k - x
        adj[v][k] = len_i_k - x
    return v

def AddJToV(adj: dict[int, dict[int, int]], v: int, j: int, limb_len: int):
    if v == j:
        new_v = v+1
        adj[new_v] = adj[v]
        for i in adj:
            if v in adj[i]:
                adj[i][new_v] = adj[i][v]
                del adj[i][v]
        del adj[v]
        v+= 1
    adj[v][j] = limb_len
    adj[j] = {}
    adj[j][v] = limb_len


if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "/datasets/test.txt"

    n = 0
    matrix = []
    with open(file_path) as f:
        n = int(f.readline().strip())
        for line in range(n):
            row = f.readline().split(" ")[:n]
            matrix.append([int(v.strip()) for v in row])

    print(AdaptivePhylogeny(matrix))




# 0 - 1 = 13
# 1 - 0 = 13
# ======
# 0 - 4 = 15
# 1 - 4 = 6
# ===
# 0  - 4 = 11
# 1 - 4 = 6
# 4 - 3 = 6
