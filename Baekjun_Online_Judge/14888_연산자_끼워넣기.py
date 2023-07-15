from itertools import permutations


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    ops = list(map(int, input().split()))

    # TODO: 연산자 순열 cases 만들기
    '''
    0,1,2,3의 index는 +, -, x, %을 의미
    '''
    target_operators = []
    for i, count in enumerate(ops):
        if count > 0:
            target_operators += [i] * count

    cases = set(permutations(target_operators, n-1))

    # TODO: 주어진 연산자로 연산 결과
    min_answer, max_answer = 1000000001, -1000000001
    for case in cases:
        temp = calculation(nums, case)
        if temp < min_answer:
            min_answer = temp
        if temp > max_answer:
            max_answer = temp

    print(max_answer)
    print(min_answer)


def calculation(nums, operators):
    temp = nums[0]
    result = 0
    for i, operator_index in enumerate(operators):

        if operator_index == 0:
            result = temp + nums[i+1]
        elif operator_index == 1:
            result = temp - nums[i+1]
        elif operator_index == 2:
            result = temp * nums[i+1]
        else:
            if result < 0:
                result = -(-temp // nums[i+1])
            else:
                result = temp // nums[i+1]
        temp = result

    return result



main()