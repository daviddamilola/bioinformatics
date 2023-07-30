def Breakpoints(p: list[str]) -> int:
    breakpoint_count = 0
    for i in range(len(p)):
        val = p[i]
        prev = "0" if i == 0 else p[i-1]
        if not isAdjacent(prev, val):
            breakpoint_count+=1
    if not isAdjacent(p[-1], str(len(p)+1)):
        breakpoint_count+=1

    return breakpoint_count

def isAdjacent(a: str, b: str) -> bool:
    return int(b) - int(a) == 1


if __name__ == "__main__":
    p_str = "+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14"
    path = "./datasets/dataset_287_6.txt"
    with open(path) as f:
        p_str = f.readline().strip()
    p = p_str.strip().split(" ")
    result = Breakpoints(p)
    with open('./results/nreakpoints.txt', 'w') as f:
        f.write(str(result))
    print("Breakpoints: ", result)
