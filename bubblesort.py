def bubble_sort(array):
  while True:
    #Assume the array is all sorted
    all_sorted = True
    
    for i in range(len(array)-1):
      # if there are unsorted elems, sort them
      if array[i]>array[i+1]:
        array[i],array[i+1]=array[i+1],array[i]
        # change all_sorted to false
        # and we should check the array again in the next loop
        all_sorted = False

    # if there is no unsorted elems, just return
    if all_sorted:
      return

a = [2,6,1,9,4,8,2]
bubble_sort(a)
print(a)
