import sys
read = sys.stdin.readline


def main():
    n = int(read())
    arr = []
    for _ in range(n):
        arr.append(int(read()))

    insertion_sort(arr)
    for i in range(n):
        print(arr[i])

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

main()