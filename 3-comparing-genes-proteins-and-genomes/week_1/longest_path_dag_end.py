from collections import defaultdict, OrderedDict

def LongestPathDAG(out_graph: dict, end: str, queue: list[int]):
    max_values = defaultdict(int)
    queue = []

    max_path_sum = 0

    if not out_graph[end]:
        return 0, queue
    for node in out_graph[end]:
        new_queue = [node]+[queue]
        path_sum = LongestPathDAG(out_graph, node, new_queue)
        if path_sum > max_path_sum:
            max_path_sum = path_sum
            queue = new_queue
    


path = './datasets/dataset_0.txt'

if __name__ == "__main__":
    with open(path) as f:
        start = f.readline().strip()
        end = f.readline().strip()

        in_graph = OrderedDict()
        out_graph = defaultdict(dict)
        for line in f:
            in_, right = line.strip().split('->')
            out, weight = right.split(':')

            in_ = in_
            out = out
            weight = int(weight)

            if in_ in in_graph:
                in_graph[in_][out] = weight
            else:
                in_graph[in_] = { out: weight}

            out_graph[out][in_] = weight

    print("??? Ins...", in_graph)
    print("??? Outs...", out_graph)
    print("??? start... end", start, end)
    max_value, ordering = LongestPathDAG(out_graph, in_graph, "start", "end")
    with open('./results/longest_path_dag.txt', 'w') as f:
        f.write(str(max_value) + "\n")
        f.write("->".join(map(str, ordering)))