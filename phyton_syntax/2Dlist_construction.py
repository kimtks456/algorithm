# arr = [[1,2,3,4]] * 3
# [[1, 2, 10, 4], [1, 2, 10, 4], [1, 2, 10, 4]]

arr = [[1,2,3,4] for _ in range(3)]
arr[1][2] = 10
arr
# [[1, 2, 3, 4], [1, 2, 10, 4], [1, 2, 3, 4]]

# * num 이렇게 생성하면, 한곳만 바꿔도 해당 열 다 반영됨. 
# list comprehension 이용할것.

# Useful to know: when you create a list of a specific size, 
# for instance using the expression [ None ] * 1000 or [0] * 1000,
# the list will be created without any extra space,
# so the capacity will be equal to the size.
