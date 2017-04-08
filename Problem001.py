def mult(limit):
  sum = 0
  for i in range(limit):
    if (i % 3 == 0) or (i % 5 == 0):
      sum += 1
  return sum

def multlist(limit):
  li = [x for x in range(limit) if x % 3 == 0 or x % 5 == 0]
  return len(li)

print(mult(500))
print(listver(500))


