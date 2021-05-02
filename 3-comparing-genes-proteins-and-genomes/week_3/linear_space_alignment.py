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
        stack.append(direction)
        LinearSpaceAlignment(v, w, next_node[0], bottom, next_node[1], right, indel, stack)

def OutputLCS(backtrack, v, w):
    v_result = "" 
    w_result = "" 
    for i, direction in enumerate(backtrack):
        if direction == "+":
            v_result += v[i]
            w_result += v[i]
        elif direction == "-":
            v_result += v[i]
            w_result += "-"
        else:
            v_result += "-"
            w_result += w[i]
    
w = "MEANLY"
v = "PLEASANTLY"
stack = []
LinearSpaceAlignment(v, w, 0, len(v), 0, len(w), 5, stack)
result = list("".join(filter(lambda x: x, stack)))
print(OutputLCS(result, v, w))