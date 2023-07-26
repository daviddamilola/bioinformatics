from middle_edge_new_full import MiddleEdge

def ModifiedMiddleEgde(v, w, top, bottom, left, right, m, mm, indel):
    mid_node, next_node, direction = MiddleEdge(v[top:bottom], w[left:right], m, mm, indel) 
    return (mid_node[0]+top, mid_node[1]+left), (next_node[0]+top, next_node[1]+left), direction

def LinearSpaceAlignment(v, w, top, bottom, left, right, m, mm, indel, stack):
    # print()
    # print(">> ", top, bottom, left, right)
    if left == right:
        result = (bottom - top) * ["|"]
        # if len(result) > 0:
        #     print("Adding from left && right", top, bottom, "=>", result)
        stack.extend(result)
    elif top == bottom:
        result = (right - left) * ["-"]
        # if len(result) > 0:
        #     print("Adding from top && bottom", left, right, "=>", result)
        stack.extend(result)
    # elif bottom - top == 1 or right - left == 1:
    #     return
    else:
        mid_node, next_node, direction = ModifiedMiddleEgde(v, w, top, bottom, left, right, m, mm, indel)
        # print("Top {} bottom {}, left {} right {}, direction {}, middle {}".format(
        #     top, bottom, left, right, direction, (mid_node[0], mid_node[1])))
        LinearSpaceAlignment(v, w, top, mid_node[0], left, mid_node[1], m, mm, indel, stack)
        stack.append(direction)
        LinearSpaceAlignment(v, w, next_node[0], bottom, next_node[1], right, m, mm, indel, stack)

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

def OutputLCS_New(backtrack, v, w):
    result_v = ""
    result_w = ""
    i, j = len(v), len(w)
    for backtrack_i, backtrack_val in  enumerate(reversed(backtrack)):
        if backtrack_val == "+":
            result_v = v[i-1] + result_v 
            result_w = w[j-1] + result_w
            i-=1
            j-=1
        elif backtrack_val == "|":
            result_v = v[i-1] + result_v
            result_w = "-" + result_w
            i-=1
        elif backtrack_val == "-":
            result_v = "-" + result_v
            result_w = w[j-1] + result_w
            j-=1
    if i > 0:
        result_v = v[i-1] + result_v 
        result_w = "-" + result_w
    if j > 0:
        result_w = w[j-1] + result_w 
        result_v = "-" + result_v

    return result_v, result_w

def GetAlignmentScore(v, w, m, mm, indel):
    l = len(v)
    score = 0
    for i in range(l):
        if v[i] == w[i]:
            score += m
        elif v[i] == "-" or w[i] == "-":
            score -= indel
        elif v[i] != w[i]:
            score -= mm
        else:
            raise "Got " + v[i] + w[i]
    return score 


# v = "CC"
# w = "TT"
# stack = []
# LinearSpaceAlignment(v, w, 0, len(v), 0, len(w), 1, 5, 1, stack)
# result = "".join(filter(lambda x: x, stack))
# result = result[::-1]
# print(result)
# print("Old: ", OutputLCS(result, w, v))
# print("New: ", OutputLCS_New(result, w, v))

if __name__ == "__main__":
    testing = True
    path = 'datasets/dataset_250_14.txt'
    # if testing:
    #     file_name = "_4.txt"
    #     path = '/Users/ashinzekene/Downloads/LinearSpaceAlignment/inputs/input' + file_name 
    #     solution = '/Users/ashinzekene/Downloads/LinearSpaceAlignment/outputs/output' + file_name
    with open(path) as f:
        params = f.readline().strip()
        params = params.split(" ")
        m, mm, indel = int(params[0]), int(params[1]), int(params[2])
        w = f.readline().strip()
        v = f.readline().strip()
        print(m, mm, indel)
    print("V W |", v, w)
    stack = []
    LinearSpaceAlignment(v, w, 0, len(v), 0, len(w), m, mm, indel, stack)
    print(stack)
    v, w = OutputLCS_New(stack, v, w)
    print(GetAlignmentScore(v, w, m, mm, indel))
    print(w+'\n'+ v)
    # if testing:
    #     print("---Expected---")
    #     with open(solution) as f:
    #         print(f.read())
    with open('./results/middle_edge.txt', 'w') as f:
        f.write(str(w) + "\n" + str(v))
