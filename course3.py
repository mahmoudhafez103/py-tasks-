# tuple
z = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
listt = z

_list = [i**2 for i in listt]
print(_list[:])

print(f'{22/2} kg')


def convertToKG(a):
    print(f'{a/1000}KG')


convertToKG(52000)


print("##############################################################")


# def sayhi(name):
#     print(F'hi {name}....!')


# myname = input("tell me ur name : ")
# sayhi(myname)


print("########################=>  dictionary")

x = {1: {"name": "mahmoud",
         "age": "20",
         "phone": "010666201215"},
     2: {"name": "mahmoud",
         "age": "20",
         "phone": "010666201215"},
     3: {"name": "mahmoud",
         "age": "20",
         "phone": "010666201215"},
     }
print(x[1]["name"])


def sqfunc(_list):
    _list1 = [i**2 for i in _list]
    print(_list1[:])


mylist = [2, 4, 6, 8, 10]
sqfunc(mylist)
