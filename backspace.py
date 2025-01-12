# Task about backspace.
# There's a string "o23#wry##92dq1#", where the '#' character represents pressing backspace,
# meaning the string essentially becomes "o2w92dq". Write a function to compare two such strings.

def compareBackspaced(string1: str, string2: str):
  i = len(string1) - 1
  j = len(string2) - 1
  stepi = 0
  stepj = 0
  res = len(string1) == len(string2) == 0
  while(i >= 0):
    if (string1[i] == '#'):
      stepi += 1
      i -= 1
      continue
    if (string2[j] == '#'):
      stepj += 1
      j -= 1
      continue
    if (stepi > 0 or stepj > 0):
      i -= stepi
      j -= stepj
      stepi = stepj = 0
      continue
    print(string1[i], " - ", i, " and ", string2[j], " - " ,j)
    if (string1[i] != string2[j]):
      break
    i -= 1
    j -= 1
  if (i == j == -1):
    res = True
  return res



str1 = list("o23#wry##92dq1#")
str2 = list("o2y#w92dq1#")
print(str1)
print(str2)
print(compareBackspaced(str1, str2))

