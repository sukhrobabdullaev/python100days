# mylist = ["apple", "banana", "cherry"]
#
# print(mylist)
#
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)
#
# # list constructor
#
# arr=list((1,2,'slaom'))
# print(arr)

"""
There are four collection data types in the Python programming language:

✅ List is a collection which is ordered and changeable. Allows duplicate members.
✅ Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
✅ Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
✅ Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""
# listNew = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(listNew[2:5]) #['cherry', 'orange', 'kiwi']
# print(listNew[:4]) #['apple', 'banana', 'cherry', 'orange']
# print(listNew[2:]) #["cherry", "orange", "kiwi", "melon", "mango"]
#
# print('apple' in listNew) # True
# print(listNew[-1]) # last element -1,-2,-3....
# listNew[1:3]=["blackcurrant", "watermelon"] # replacing 1,2 elements
# print(listNew)
#
# listNew.insert(4,'watermelon')
# print(listNew)
# listNew = ["apple", "banana", "cherry"]
# listNew.append('orange')
# print(listNew)

# first=[1,2,3]
# second=[4,5,6,7]
# first.extend(second)
# # print(first)
#
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)
#
# thislist.remove('apple')
# print(thislist) # ['banana', 'cherry', 'kiwi', 'orange']
#
# thislist.pop(1)
# print(thislist) # ['banana', 'kiwi', 'orange']

# thislist.clear()
# print(thislist)


# LOOP TROUGH A LIST

# items
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
#
# # indicies
# for i in range(len(thislist)):
#     print(thislist[i])
#
# # while loop
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)
#
# # fruits.sort()
# fruits.sort(reverse=True)
# print(fruits)
#
# def myfunc(n):
#   return abs(n - 50)
#
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)
#
# fruits2 = ["banana", "Orange", "Kiwi", "cherry"]
# fruits2.sort(key = str.lower)
# print(fruits2)


# Copying lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# list3 = list1 + list2
list3 = list1.extend(list2)
print(list1)