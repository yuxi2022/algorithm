def binary_search(list, item):
  # low and high keep track of which part of the list you'll search in.
  low = 0
  high = len(list) - 1

  # While you haven't narrowed it down to one element ...
  while low <= high:
    # ... check the middle element
    mid = (low + high) // 2
    guess = list[mid]
    # Found the item.
    if list[mid] == item:
      return mid
    # The guess was too high.
    if list[mid] > item:
      high = mid - 1
    # The guess was too low.
    else:
      low = mid + 1

  # Item doesn't exist
  return None



my_list = [1,3,5,7,9,11,12,14,16,18,20,34,35,37,59]
print(binary_search(my_list, 9)) # => 1
