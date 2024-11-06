# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# thistuple = ("apple",)
# print(type(thistuple))


# print(thistuple[-1],thistuple[2])
# print(thistuple[1:2])

# type conversion: tuple to list
# x=("apple","banana","cherry")
# y=list(x)
# y[1]='kiwi'
# x=tuple(y)

# print(x)


# unpacking a tuple

# fruits=("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green,yellow,red)
#
# for i in range(len(fruits)):
#     print(fruits[i])
#
# # tuple multiply
# ss = ("apple", "banana", "cherry")
# mytuple = ss * 2
#
# print(mytuple)


thistuple=[1,3,7,8,7,5,4,6,8,5]
x=thistuple.count(5)
print(x)