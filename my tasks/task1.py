# *********************************1****************

print("************task1********")
list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1[::-1])
list1.reverse()


print(list1[:])
print("\n")


# *********************************2****************

print("************task2********")
numbers = [1, 2, 3, 4, 5, 6, 7]
for i in range(0, len(numbers)):
    numbers[i] *= numbers[i]
print(numbers[:])
print("\n")
newnumbers = [i**2 for i in range(1, 8)]
print(newnumbers[:])
print("\n")

# *********************************3****************
# here is a commit
print("*************task3********")
list2 = [5, 10, 15, 20, 25, 50, 20]

countt = 0
for i in range(0, len(list2)):
    if(list2[i] == 20):
        if(countt > 0):
            pass
        else:
            countt += 1
            list2[i] = 200
print(list2[:])
