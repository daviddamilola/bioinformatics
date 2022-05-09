from middle_edge import MiddleEdge

def ModifiedMiddleEgde(v, w, top, bottom, left, right, indel):
    mid_node, next_node, direction = MiddleEdge(v[top:bottom], w[left:right], indel) 
    return (mid_node[0]+top, mid_node[1]+left), (next_node[0]+top, next_node[1]+left), direction

def LinearSpaceAlignment(v, w, top, bottom, left, right, indel, stack):
    if left == right:
        stack.append((bottom - top) * "|")
    elif top == bottom:
        stack.append((left - right) * "-")
    else:
        mid_node, next_node, direction = ModifiedMiddleEgde(v, w, top, bottom, left, right, indel)
        LinearSpaceAlignment(v, w, top, mid_node[0], left, mid_node[1], indel, stack)
        print("{} and {}, direction {}, middle ".format(
            v[top:bottom], w[left:right], direction), mid_node[0]+top, mid_node[1]+left)
        stack.append(direction)
        LinearSpaceAlignment(v, w, next_node[0], bottom, next_node[1], right, indel, stack)

def OutputLCS(backtrack, v, w):
    v_result = "" 
    w_result = "" 
    v_index = 0
    w_index = 0
    for i, direction in enumerate(backtrack):
        if direction == "+":
            v_result += v[v_index]
            w_result += w[w_index]
            v_index += 1
            w_index += 1
        elif direction == "-":
            v_result += v[v_index]
            w_result += "-"
            v_index += 1
        else:
            v_result += "-"
            w_result += w[w_index]
            w_index += 1
    return v_result, w_result


v = "MEANLY"
w = "PLEASANTLY"
stack = []
LinearSpaceAlignment(v, w, 0, len(v), 0, len(w), 5, stack)
result = "".join(filter(lambda x: x, stack))
result = result[::-1]
print(result)
print(OutputLCS(result, w, v))
