import sys
read = sys.stdin.readline

def main():
    paper = [[0 for _ in range(100)] for _ in range(100)]
    n = int(read())
    coord = []
    for _ in range(n):
        coord.append(tuple(map(int, read().split())))

    for x, y in coord:
        for j in range(x-1, x+9):
            for i in range(99-y, 89-y, -1):
                if (paper[i][j] == 0) and (0 <= i <= 99) and (0 <= j <= 99):
                    paper[i][j] = 1
    # for i in range(100):
        # print(paper[i])
    print(sum(map(sum, paper)))

main()