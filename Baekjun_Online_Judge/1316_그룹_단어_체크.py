import sys

read = sys.stdin.readline


def main():
    n = int(read())
    words = []
    for _ in range(n):
        words.append(read().rstrip())

    result = n
    for i in range(n):
        dup = set()
        target = words[i]
        dup.add(target[0])

        if len(target) >= 2:
            for j in range(1, len(target)):
                if (target[j] != target[j - 1]) and target[j] in dup:
                    result -= 1
                    break
                dup.add(target[j])
    print(result)


main()
