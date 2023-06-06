import sys
read = sys.stdin.readline


def main():
    n = int(read())
    words = set()
    for _ in range(n):
        words.add(read().strip())

    sorted_words = sorted(words, key=lambda x: (len(x), x))

    for i in range(len(sorted_words)):
        print(sorted_words[i])


main()