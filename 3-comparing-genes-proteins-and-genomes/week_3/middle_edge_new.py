def GetScoreMatrix(v, w, m, mm, indel):
    lv = len(v)
    lw = len(w)
    scores_matrix = [[0] * (lw+1) for i in range(lv+1)]
    for i in range(1, lv+1):
        scores_matrix[i][0] = scores_matrix[i-1][0] - indel
    for j in range(1, lw+1):
        scores_matrix[0][j] = scores_matrix[0][j-1] - indel
    
    for i in range(1, len(scores_matrix)):
        for j in range(1, len(scores_matrix[0])):
            symbol_a = v[i-1]
            symbol_b = w[j-1]
            match_mismatch = scores_matrix[i-1][j-1] - mm
            if symbol_a == symbol_b:
                match_mismatch = scores_matrix[i-1][j-1] + m
            insertion = scores_matrix[i-1][j] - indel
            deletion = scores_matrix[i][j-1] - indel

            scores_matrix[i][j] = max(insertion, deletion, match_mismatch)
    return scores_matrix

def get_source_sink(from_source, from_sink, mid):
    from_source_m = [x[mid] for x in from_source]
    from_source_n = [x[mid+1] for x in from_source]

    from_sink_ = [list(reversed(x)) for x in from_sink]
    from_sink_m = [x[mid] for x in from_sink_]
    from_sink_n = [x[mid+1] for x in from_sink_]

    return ((from_source_m, from_source_n), (list(reversed(from_sink_m)), list(reversed(from_sink_n))))

def MiddleEdge(v, w, m, mm, indel):
    lw = len(w)
    middle_col_index = lw//2

    w_mid_1 = w[0:middle_col_index+1]
    w_mid_2 = w[lw:middle_col_index-1:-1]

    from_source = GetScoreMatrix(v, w, m, mm, indel)
    from_sink = GetScoreMatrix(v[::-1], w[::-1], m, mm, indel)

    if __name__ == "__main__":
        print('MID', middle_col_index)
        print("from_source", from_source)
        print("from_sink", from_sink)

    source, sink = get_source_sink(from_source, from_sink, middle_col_index)
    if __name__ == "__main__":
        print("source", source)
        print("sink", sink)

    from_sink = from_sink[::-1]

    middle_column = [source[0][i] + sink[0][i]
                     for i in range(len(v)+1)]
    next_column = [source[1][i] + sink[1][i]
                   for i in range(len(from_source))]
    # print("middle col", middle_column)
    # print("next_column", next_column)


    mid_index = middle_column.index(max(middle_column))
    print("Middle mid index", mid_index, max(middle_column))

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
    w = "G"
    m = 1
    mm = 1
    indel = 2
    # v = "MEASLY"
    # w = "PLEASANTLY"
    # v = "CGGAGTGCC"
    # w = "A"
    v = "GGG"
    w = "GAACGATTG"
    m = 1
    mm = 5
    indel = 1
    path = 'datasets/dataset_250_12_.txt'
    # with open(path) as f:
    #     params = f.readline().strip()
    #     params = params.split(" ")
    #     m, mm, indel = int(params[0]), int(params[1]), int(params[2])
    #     w = f.readline().strip()
    #     v = f.readline().strip()
    #     print(m, mm, indel)
    #     print(v, w)
    edge1, edge2, _ = MiddleEdge(v, w, m, mm, indel)
    print(edge1, edge2, _)
    # with open('./results/middle_edge_new.txt', 'w') as f:
    #     f.write("{} {}\n{} {}".format(edge1[0], edge1[1], edge2[0], edge2[1]))
