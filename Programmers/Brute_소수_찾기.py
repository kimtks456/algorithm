from itertools import permutations as pm


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    visited = set()

    for n in range(1, len(numbers) + 1):
        for case in pm(numbers, n):
            temp = int(''.join(map(str, case)))

            if isPrime(temp) and temp not in visited:
                answer += 1
                visited.add(temp)
    return answer