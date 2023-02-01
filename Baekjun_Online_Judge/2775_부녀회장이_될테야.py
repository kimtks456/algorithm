import sys

read = sys.stdin.readline


def main():
    T = int(read())
    floors, rooms = [], []
    for _ in range(T):
        floors.append(int(read()))
        rooms.append(int(read()))

    capacity = [[0 for _ in range(max(rooms) + 1)] for _ in range(max(floors) + 1)]
    capacity[0] = [i for i in range(max(rooms) + 1)]

    for i in range(1, max(floors) + 1):
        for j in range(1, max(rooms) + 1):
            capacity[i][j] = capacity[i][j-1] + capacity[i-1][j]

    for i in range(T):
        print(capacity[floors[i]][rooms[i]])

main()
