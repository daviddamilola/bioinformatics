def isUniversalBinary(val: str, x: int) -> bool:
    arr = []
    length = 2 ** x
    for i in range(length):
        arr.append(0)
    for i in range(len(val)-x-1):
        binaryStr = str(val[i:i+x])
        decimalStr = int(binaryStr, 2)
        arr[decimalStr]+=1
    for val in arr:
        if val != 1:
            return False
    return True