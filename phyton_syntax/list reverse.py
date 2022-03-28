# list.reverse() 반환 없이 list 역전. list 제공 함수
# l2 = list.reversed() 반환 있음. 내장 함수. tuple, string도 역전된 값 반환
# 근데 list에 대해 reversed하면 listreverseiterator라는 객체를 반환.
# 그저 list를 역전된 순서로 탐색(traverse)할 수 있는 객체를 반환한다는 의미.
# list로 쓰려면 list()로 list화 시키면 되는데, 아래 예시를 보면, 역전해서 바꿔놔도 함수 나가면 reverse 풀림.
# 탐색만 역전된 순서로하고 실제 list 값을 바꾼것이 아니기에 함수 끝나면 원래 list 값을 가져오는 듯.
# 따라서 list.reverse()를 이용해 list객체 자체의 순서를 바꿔야 함. 속도도 이게 더 빠름
# (https://stackoverflow.com/questions/6810036/whats-better-the-reverse-method-or-the-reversed-built-in-function)


# Function to print the matrix
def print_matrix(mat, size):
  for i in range(0, size):
    for j in range(0, size):
      print ("{:<2}".format(mat[i][j]), end = ' ')
    print ("")

# You just need to implement this function
def rotate_matrix(mat, size):
  """
  An Inplace function to rotate N x N matrix by 90 degrees in
  anti-clockwise direction
  
  >>> mat = [[1, 2, 3],
  ...        [4, 5, 6],
  ...        [7, 8, 9]]
  >>> rotate_matrix(mat, 3)
  >>> print_matrix(mat, 3)
  3 6 9 
  2 5 8 
  1 4 7 
  >>> mat = [[1, 2],
  ...        [4, 5]]
  >>> rotate_matrix(mat, 2)
  >>> print_matrix(mat, 2)
  2 5 
  1 4 
  >>> mat = [[ 1,  2,  3,  4],
  ...        [ 5,  6,  7,  8],
  ...        [ 9, 10, 11, 12],
  ...        [13, 14, 15, 16]]
  >>> rotate_matrix(mat, 4)
  >>> print_matrix(mat, 4)
  4 8 12 16 
  3 7 11 15 
  2 6 10 14 
  1 5 9 13 
  >>> mat = [[1]]
  >>> rotate_matrix(mat,1)
  >>> print_matrix(mat,1)
  1 
  """
  # YOUR CODE HERE
  
  mat = list(reversed(mat))
  # mat.reverse()
  
  for i in range(size):
    for j in range(size-i-1):
      mat[i][j], mat[size-1-j][size-1-i] = mat[size-1-j][size-1-i], mat[i][j]
  print_matrix(mat, size)
  
# 00 - 33
# 01 - 12
# 02 - 13
# 03 - 03

# 10 - 32
# 11 - 22

m = [[ 1,  2,  3,  4],
     [ 5,  6,  7,  8],
     [ 9, 10, 11, 12],
     [13, 14, 15, 16]]


print("###### m in func #######")
rotate_matrix(m,4)
print("###### m out of func #######")
print_matrix(m,4)

###### 출력문 #######
# ###### m in func #######
# 4  8  12 16 
# 3  7  11 15 
# 2  6  10 14 
# 1  5  9  13 
# ###### m out of func #######
# 1  5  9  13 
# 2  6  10 14 
# 3  7  11 15 
# 4  8  12 16 
