import random, time

limit = int(input("Enter Limit: "))
to_sort = random.sample(range(0, limit), limit)
#print("Generated List: " + str(to_sort))
index = 0
start = time.time()
while index < len(to_sort):
    if index == 0 or to_sort[index] >= to_sort[index-1]:
        index += 1
        #print("if" + str(index))
    else:
        #print("else" + str(index) + ": " + str(to_sort))
        num = to_sort[index]
        num2 = to_sort[index-1]
        to_sort[index] = num2
        to_sort[index-1] = num
        index = index - 1
finish = time.time()
print("List sorted in " + str(finish-start) + "s : " + str(to_sort))
