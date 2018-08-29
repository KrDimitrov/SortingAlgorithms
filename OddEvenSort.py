import random, time

limit = int(input("Enter Limit: "))

to_sort = random.sample(range(0, limit), limit)

sorted = False
start = time.time()
while not sorted:
    sorted = True

    for index,value in enumerate(to_sort):
        index = index+1
        try:
            to_sort[index+1]
        except IndexError:
            break;

        if to_sort[index] > to_sort[index+1]:
            temp = to_sort[index]
            to_sort[index] = to_sort[index+1]
            to_sort[index+1] = temp
            sorted = False
#    print(to_sort)
    for index,value in enumerate(to_sort, start=0):
        try:
            to_sort[index+1]
        except IndexError:
            break;
        if to_sort[index] > to_sort[index+1]:
            temp = to_sort[index]
            to_sort[index] = to_sort[index+1]
            to_sort[index+1] = temp
            sorted = False
finished = time.time()
print("List Sorted in " + str(finished-start) + "s : " + str(to_sort))

