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
