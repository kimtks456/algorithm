def solution(number, k):
    nums = list(map(int, number))
    stack = [nums[0]]
    count = 0

    for i in range(1, len(nums)):
        while stack and stack[-1] < nums[i] and count < k:
            stack.pop()
            count += 1
        stack.append(nums[i])

    while count < k:
        stack.pop()
        count += 1

    answer = ''.join(list(map(str, stack)))
    return answer

# print(solution("1231234", 3))
# print(solution("4177252841", 4))