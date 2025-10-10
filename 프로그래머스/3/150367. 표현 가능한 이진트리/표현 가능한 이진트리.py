def solution(numbers):
    answer = []
    for number in numbers:
        binStr = bin(number)[2:]
        padded = paddedBinStr(binStr)
        center = len(padded) // 2
        
        if isBinTree(padded):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer

def isBinTree(tree):
    center = len(tree) // 2
    
    if len(tree) == 1:
        return True
    
    if len(tree) == 3:
        if tree[center] == '1':
            return True
        else:
            return tree == '000'
    
    if tree[center] == '0':
        return tree == '0' * len(tree)
    
    return isBinTree(tree[:center]) and isBinTree(tree[center+1:])


def paddedBinStr(target):
    level = 1
    while True:
        if 2 ** level - 1 < len(target):
            level += 1
        else:
            break
    return '0' * (2 ** level - 1 - len(target)) + target
