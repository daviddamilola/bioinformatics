from colored_edges import ColoredEdges, FormatChromosome
from chromose_to_cycle import ChromosomeToCycle

def Cycles(chromosome_a_str: str, chromosome_b_str: str) -> int:
    circles = 0
    chromosome_a = FormatChromosome(chromosome_a_str)
    chromosome_b = FormatChromosome(chromosome_b_str)
    unvisited = ChromosomeToCycle(chromosome_a_str[1:-1].replace(")(", " ").split(" "))
    edge_length = len(unvisited)
    visited = []
    edges_a = ColoredEdges(chromosome_a)
    edges_b = ColoredEdges(chromosome_b)
    graph_a = IndegreesFromEdge(edges_a)
    graph_b = IndegreesFromEdge(edges_b)
    while len(visited) < edge_length:
        graph = "A"
        current_edge = unvisited[0]
        while not (current_edge in visited):
            unvisited.remove(current_edge)
            visited.append(current_edge)
            current_graph = graph_a if graph == "A" else graph_b
            current_edge = current_graph[current_edge]
            graph = "B" if graph == "A" else "A"
            current_graph = graph_b
        circles += 1

    return circles

def Blocks(chromosome_a_str: str) -> list[str]:
    return chromosome_a_str[1:-1].replace(")(", " ").split(" ")

def TwoBreakDistance(chromosome_a_str: str, chromosome_b_str: str) -> int:
    blocks = Blocks(chromosome_a_str)
    cycles = Cycles(chromosome_a_str, chromosome_b_str)
    return len(blocks) - cycles
            

def IndegreesFromEdge(edges: list[tuple[int]]) -> dict[int, int]:
    indegrees: dict[int, int] = dict()
    for edge in edges:
        indegrees[edge[0]] = edge[1]
        indegrees[edge[1]] = edge[0]
    return indegrees

if __name__ == "__main__":
    chromosome_a = "(+1 +2 +3 +4 +5 +6)"
    chromosome_b = "(+1 -3 -6 -5)(+2 -4)"
    chromosome_a = "(+1 -3 -6 -5)(+2 -4)"
    chromosome_b = "(+1 +2 +3 +4 +5 +6)"
    path = "./datasets/dataset_288_4.txt"
    with open(path) as f:
        chromosome_a = f.readline().strip()
        chromosome_b = f.readline().strip()
    result = TwoBreakDistance(chromosome_a, chromosome_b)
    print(result)
    with open('./results/cycles.txt', 'w') as f:
        f.write(str(result)[1:-1])
