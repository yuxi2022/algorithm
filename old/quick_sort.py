my_list = [1,3,5,7,9]

sum =0

for i in range(len(my_list)):
    sum = sum + my_list[i]
print(sum)


def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    #less = [i for i in array[1:] if i <= pivot]

    less = []
    greater = []

    for i in array[1:]:
        if i<=pivot:
            less.append(i)
        if i>pivot:
            greater.append(i)


    # sub-array of all the elements greater than the pivot
    #greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3,7,3,7,34,9]))
