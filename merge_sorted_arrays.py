def merge_arr(first, second):
  res = [0] * (len(first) + len(second)) 
  i = j = 0

  while i + j < len(res):
    if i < len(first) and (j >= len(second) or first[i] < second[j]):
      res[i + j] = first[i]
      i += 1
    else:
      res[i + j] = second[j]
      j += 1
  return res


one = [1, 3, 5, 7, 20, 39, 10000]
two = [2, 4, 9, 11, 19, 33, 1000, 1239, 31333]

print(merge_arr(one, two))