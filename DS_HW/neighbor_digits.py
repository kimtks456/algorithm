def neighbor_digits(num, prev_digit=-1):
  """
  Returns the number of digits in num that have the same digit to its right
  or left.
  >>> neighbor_digits(111)
  3
  >>> neighbor_digits(123)
  0
  >>> neighbor_digits(112)
  2
  >>> neighbor_digits(1122)
  4
  """
  # YOUR CODE HERE
  a = str(num)
  cnt = 0
  for i in range(len(a)):
    check = a[i]

    if i == 0:
      if check == a[i+1]:
        cnt += 1
        continue
      else:
        continue

    elif i == len(a)-1:
      if check == a[i-1]:
        cnt += 1
        break
      else:
        break
    else:
      if check == a[i+1] or check == a[i-1]:
        cnt += 1
        continue
      else :
        continue

  return cnt

#이 간단한걸 푸는데 6시간이 걸림.,. (22.3.21)
