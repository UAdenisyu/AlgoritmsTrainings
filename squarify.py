# Task - Given a sorted array [-7, -4, -1, 3, 6, 10]
# Iterate through the array, square each element, and ensure the result remains sorted.


def squarify(arr: list[int]):
  res_arr = [0] * len(arr)
  right = len(arr) - 1
  left = 0
  for i in range(len(arr) - 1, -1, -1):
    if abs(arr[right]) > abs(arr[left]):
      res_arr[i] = arr[right] ** 2
      right -= 1
    else:
      res_arr[i] = arr[left] ** 2
      left += 1
  return res_arr

arr1 = [-7, -5, -4, -1, 0, 1, 3, 5, 6, 10]
print(squarify(arr1))
