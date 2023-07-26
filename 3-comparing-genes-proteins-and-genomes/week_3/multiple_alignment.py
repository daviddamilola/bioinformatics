def MultipleAlignment(u, v, w):
    matrix = [[[0 for i in range(len(u)+1)] for i in range(len(v)+1)] for i in range(len(w)+1)]
    backtrack = [[['---' for i in range(len(u)+1)] for i in range(len(v)+1)] for i in range(len(w)+1)]

    # for i in range(1, len(u)):
    #     matrix[i][0][0] = 0
    # for j in range(1, len(v)):
    #     matrix[0][j][0] = 0
    # for k in range(1, len(w)):
    #     matrix[0][0][k] = 0

    for i in range(0, len(u)):
        for j in range(0, len(v)):
            for k in range(0, len(w)):
                add = 0
                if u[i] == v[j] == w[k]:
                    add = 1
                sum = max(
                    matrix[k+1][j+1][i],
                    matrix[k+1][j][i+1],
                    matrix[k][j+1][i+1],
                    matrix[k][j][i+1],
                    matrix[k][j+1][i],
                    matrix[k+1][j][i],
                    matrix[k][j][i] + add
                )
                matrix[k+1][j+1][i+1] = sum
                if sum == matrix[k][j][i] + add:
                    backtrack[k+1][j+1][i+1] = '+++'
                elif sum == matrix[k+1][j+1][i]:
                    backtrack[k+1][j+1][i+1] = '--+'
                elif sum == matrix[k+1][j][i+1]:
                    backtrack[k+1][j+1][i+1] = '-+-'
                elif sum == matrix[k][j+1][i+1]:
                    backtrack[k+1][j+1][i+1] = '+--'
                elif sum == matrix[k][j][i+1]:
                    backtrack[k+1][j+1][i+1] = '++-'
                elif sum == matrix[k][j+1][i]:
                    backtrack[k+1][j+1][i+1] = '+-+'
                elif sum == matrix[k+1][j][i]:
                    backtrack[k+1][j+1][i+1] = '-++'
    return matrix, backtrack

def Backtrack(backtrack, u, v, w):
    u_align = ""
    v_align = ""
    w_align = ""
    i = len(u)
    j = len(v)
    k = len(w)
    print()
    while i > 0 and j > 0 and k > 0:
        value = backtrack[k][j][i]
        value_k = value[0]
        value_j = value[1]
        value_i = value[2]
        if value_i == "-":
            u_align = "-" + u_align
        else:
            u_align = u[i-1] + u_align
            i-=1
        if value_j == "-":
            v_align = "-" + v_align
        else:
            v_align = v[j-1] + v_align
            j-=1
        if value_k == "-":
            w_align = "-" + w_align
        else:
            w_align = w[k-1] + w_align
            k-=1
    while i > 0:
        u_align = u[i-1] + u_align
        i-=1
    while j > 0:
        v_align = v[j-1] + v_align
        j-=1
    while k > 0:
        w_align = w[k-1] + w_align
        k-=1
    l = max(len(u_align), len(v_align), len(w_align))
    u_align = "-" * (l-len(u_align)) + u_align
    v_align = "-" * (l-len(v_align)) + v_align
    w_align = "-" * (l-len(w_align)) + w_align

    return u_align, v_align, w_align

if __name__ == "__main__":
    u = "CCAATACGAC"
    v = "GCCTTACGCT"
    w = "CCCTAGCGGC"
    # CCAATACGAC, GCCTTACGCT, and CCCTAGCGGC
    # CCAATACGAC, GCCTTACGCT, and CCCTAGCGGC
    path = './datasets/dataset_251_5.txt'
    # with open(path) as f:
    #     u = f.readline().strip()
    #     v = f.readline().strip()
    #     w = f.readline().strip()
    print(u)
    print(v)
    print(w)
    matrix, backtrack = MultipleAlignment(u, v, w)
    str_results = "\n".join(Backtrack(backtrack, u, v, w))
    print(matrix[-1][-1][-1])
    print(str_results)
    # with open('./results/multiple_alignment.txt', 'w') as f:
    #     f.write(str(matrix[-1][-1][-1]))
    #     f.write("\n")
    #     f.write(str_results)

