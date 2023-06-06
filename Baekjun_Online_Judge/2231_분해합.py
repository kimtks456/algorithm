import sys
read = sys.stdin.readline


def main():
    n = int(read())
    for i in range(1, n + 1):
        # 터무니없이 작은 값들은 뛰어넘으면 좋겠지만, 그때도 digit_counter를 써야하므로 그냥 다 계산.
        temp = i + digit_counter(i)
        if n == temp:
            print(i)
            return 0
    print(0)
    return 0

def digit_counter(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


main()