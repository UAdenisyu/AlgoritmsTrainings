# There is a pool with water and walls. The height of the wall is defined by a number (meters).
# Determine in the pool [9, 0, 8, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4] the indices of the two boundaries that enclose the maximum water area.
# (between 9 and 8: 81m of water, between 8 and 4: 43m, and between 4 and 4: 4*8m of water.)


def find_biggest_water_pool(base_pool: list[int]):
  biggest_pool = 0
  section = 0
  left, right = 0, 1
  while (left < right and right < len(base_pool)):
    if (base_pool[right] == 0): 
      section += 1
    else:
      section_water = section * min(base_pool[left], base_pool[right])
      if (biggest_pool < section_water):
        biggest_pool = section_water
      section = 0
      left = right
    right += 1
      
  return biggest_pool


pool = [9, 0, 8, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4]
print(find_biggest_water_pool([9, 0, 8, 0, 0, 0, 6, 0, 5, 0, 0, 0, 4, 0, 0, 7]))
print(find_biggest_water_pool([10, 0, 0, 8, 0, 0, 5, 0, 0, 3, 0, 0, 6, 0, 0, 9]))
print(find_biggest_water_pool([7, 0, 6, 0, 0, 9, 0, 4, 0, 0, 0, 3, 0, 2, 0, 8]))
print(find_biggest_water_pool([8, 0, 0, 0, 10, 0, 0, 0, 6, 0, 0, 4, 0, 0, 9, 0]))
print(find_biggest_water_pool([12, 0, 0, 0, 0, 9, 0, 0, 4, 0, 0, 0, 10, 0, 0, 7]))
print(find_biggest_water_pool([15, 0, 0, 0, 10, 0, 5, 0, 0, 8, 0, 0, 0, 7, 0, 13]))
print(find_biggest_water_pool([20, 0, 0, 0, 0, 0, 15, 0, 0, 10, 0, 0, 5, 0, 0, 20]))
print(find_biggest_water_pool([6, 0, 0, 0, 9, 0, 0, 0, 8, 0, 0, 0, 3, 0, 0, 5]))
print(find_biggest_water_pool([18, 0, 0, 0, 0, 5, 0, 0, 0, 9, 0, 0, 0, 12, 0, 18]))
print(find_biggest_water_pool([25, 0, 0, 20, 0, 0, 15, 0, 0, 10, 0, 0, 5, 0, 0, 25]))

