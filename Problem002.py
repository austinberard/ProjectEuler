def evenfibs(limit):
  a = 1
  b = 1
  sum = 0

  while b < limit:
    temp = b
    if b % 2 == 0:
      sum += b
    b += a
    a = temp
  return sum


print(evenfibs(4000000))

