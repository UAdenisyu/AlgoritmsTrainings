import time
import random

large_sorted_list = list(range(10**7))
large_unsorted_list = random.shuffle(large_sorted_list)
target = 7839289

def binary_search(list, t, left = 0, right = None):
  if right is None:
    right = len(list) - 1
  if left > right:
    return 'not found'
  if left == right:
    return 'done!'
  mid = (left + right) // 2
  if list[mid] == target:
    return mid
  elif list[mid] < target:
    return binary_search(list, t, mid + 1, right)
  else:
    return binary_search(list, t, left, mid)

start_time1 = time.time()
large_sorted_list.sort() 
result = binary_search(large_sorted_list, target)
print(result)
end_time1 = time.time() # n * log(n)

start_time2 = time.time()
result = large_sorted_list.index(target)
end_time2 = time.time() # n

print(f"Binary find passed for: {end_time1 - start_time1:.6f} seconds")
print(f"Plain find passed for: {end_time2 - start_time2:.6f} seconds")
print(f"Binary find is faster in {round((end_time2 - start_time2) / (end_time1 - start_time1))} times!!!!")
