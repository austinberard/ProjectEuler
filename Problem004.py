def palindrome(n):
  if str(n) == str(n)[::-1]:
    return True
  return False


def largestPalidrome():
  return max(i*j
    for i in range(999, 0, -1)
      for j in range(999, 0, -1)
        if palindrome(i*j))


print(largestPalidrome())
