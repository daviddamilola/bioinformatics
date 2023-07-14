def GetScoreMatrix(v, w, m, mm, indel):
    lv = len(v)
    lw = len(w)
    previous_matrix = [0] * (lv+1)
    current_matrix = [0] * (lv+1)
    for i in range(1, lv+1):
        current_matrix[i] = current_matrix[i-1] - indel

    for j in range(1, lw+1):
        previous_matrix = current_matrix.copy()
        current_matrix[0] = -indel * j
        for i in range(1, lv+1):
            v_val = v[i-1]
            w_val = w[j-1]

            insertion = previous_matrix[i] - indel
            deletion = current_matrix[i-1] - indel
            match_mismatch = previous_matrix[i-1] - mm
            if v_val == w_val:
                match_mismatch = previous_matrix[i-1] + m

            current_matrix[i] = max(insertion, deletion, match_mismatch)

    matrix = [[previous_matrix[i], current_matrix[i]] for i in range(lv+1)]
    return matrix

def log_source_sink(from_source, from_sink):
    from_source_m = [x[0] for x in from_source]
    from_source_n = [x[1] for x in from_source]

    from_sink_m = [x[0] for x in reversed(from_sink)]
    from_sink_n = [x[1] for x in reversed(from_sink)]
    print("from_source", from_source_m, from_source_n)
    print("from_sink", from_sink_m, from_sink_n)
    print()

def MiddleEdge(v, w, m, mm, indel):
    lw = len(w)
    middle_col_index = lw//2

    w_mid_1 = w[0:middle_col_index+1]
    w_mid_2 = w[lw:middle_col_index-1:-1]

    from_source = GetScoreMatrix(v, w_mid_1, m, mm, indel)
    from_sink = GetScoreMatrix(v[::-1], w_mid_2, m, mm, indel)

    print("W 1", w_mid_1)
    print("W 2", w_mid_2)

    from_sink = from_sink[::-1]

    middle_column = [from_source[i][0] + from_sink[i][1]
                     for i in range(len(v)+1)]
    next_column = [from_source[i][1] + from_sink[i][0]
                   for i in range(len(from_source))]


    mid_index = middle_column.index(max(middle_column))
    # mid_index

    insertion = next_column[mid_index]

    if mid_index == len(middle_column) - 1:
        return (mid_index, middle_col_index), (mid_index-1, middle_col_index+1), "-"
    deletion = middle_column[mid_index + 1]
    match_mismatch = next_column[mid_index + 1]
    max_value = max(insertion, deletion, match_mismatch)

    if max_value == insertion:
        return (mid_index, middle_col_index), (mid_index, middle_col_index+1), "-"
    elif max_value == deletion:
        return (mid_index, middle_col_index), (mid_index+1, middle_col_index), "|"
    else:
        return (mid_index, middle_col_index), (mid_index+1, middle_col_index+1), "+"


if __name__ == "__main__":
    v = "GAT"
    w = "GAGA"
    indel = 2
    # v = "MEANLY"
    # w = "PLEASANTLY"
    # indel = 5
    m = 1
    mm = 1
    path = 'datasets/dataset_250_12_.txt'
    with open(path) as f:
        params = f.readline().strip()
        params = params.split(" ")
        m, mm, indel = int(params[0]), int(params[1]), int(params[2])
        w = f.readline().strip()
        v = f.readline().strip()
        print(m, mm, indel)
        print(v, w)
    edge1, edge2, _ = MiddleEdge(v, w, m, mm, indel)
    print(edge1, edge2, _)
    with open('./results/middle_edge_new.txt', 'w') as f:
        f.write("{} {}\n{} {}".format(edge1[0], edge1[1], edge2[0], edge2[1]))
