import math

def LimbLength(matrix: list[list[int]], j: int, n: int) -> int:
    min_limb_len = math.inf
    n == len(matrix) if n == None else n
    for i in range(n):
        for k in range(n):
            if i == j or k == j or i == k:
                continue
            limb_len = math.floor((matrix[i][j] + matrix[k][j] - matrix[i][k]) / 2)
            min_limb_len = min(limb_len, min_limb_len)
    return min_limb_len

def calculateLimbLength(distMatrix, j, n):
    limbLength = float('inf')
    if j > 0:
        i = j - 1
    else:
        i = j + 1
    for k in range(n):
        if i != k and k != j:
            currLength = (distMatrix[i][j] + distMatrix[j][k] - distMatrix[i][k])//2
            print("Their Limb len: {}, i: {}, k: {}".format(currLength, i, k))
            if currLength < limbLength:
                limbLength = currLength
                currIndex = (i, k)
    return limbLength, currIndex[0], currIndex[1]

if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "/datasets/test.txt"

    n = 0
    matrix = []
    with open(file_path) as f:
        n = int(f.readline().strip())
        j = int(f.readline().strip())
        for line in range(n):
            row = f.readline().split(" ")[:n]
            matrix.append([int(v.strip()) for v in row])

    limb_length = LimbLength(matrix, j, n)
    print("Limb length", limb_length)
    limb_length = calculateLimbLength(matrix, j, n)
    print("Limb length", limb_length)

    # result_path = dir_path + "/results/limb_length.txt"
    # with open(result_path, 'w') as f:
    #     f.write(str(limb_length))

