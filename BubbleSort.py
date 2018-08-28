import random
import time

limit = int(input("Enter List limit: "))
to_sort = random.sample(range(1, limit), limit-1)

start = time.time()
while 1:
    swapped = False
    for index,value in enumerate(to_sort):
        num = to_sort[index]
        try:
            num2 = to_sort[index+1]
        except IndexError:
            break
        if num2 < num:
            swapped = True
            to_sort[index] = num2
            to_sort[index+1] = num
    if not swapped:
        finished = time.time()
        break
    if swapped:
        continue
print("Sorted List in " + str(finished-start) + ": " + str(to_sort))
