import sys
read = sys.stdin.readline

def main():
    n, m = map(int, read().split())
    matN, matM = [], []
    for _ in range(n):
        matN.append(list(map(int, read().split())))
    for _ in range(n):
        matM.append(list(map(int, read().split())))

    for i in range(n):
        for j in range(m):
            matN[i][j] += matM[i][j]
            print(matN[i][j], end=" ")
        # if i != n-1:
        print("")

main()