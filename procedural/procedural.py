# DRY - don't repeat yourself.
# Algorithms
# Big-O
# Pure functions
# Maps take all objects in a list and applies a function
# Filters do the same but take the results and creates a new list with only the true values
# Comprehensions



# PALINDROME

# str='racecar'

# def is_palindrome(str):
#     start_index=0
#     end_index=len(str)-1
#
#     while start_index < end_index:
#         if str[start_index] != str[end_index]:
#             return False
#         start_index += 1
#         end_index -= 1
#     return True
#
# print(is_palindrome('racecar'))

# Two ways to reverse a string in Python

str='salom'
print(str[::-1])

def str_rev(str):
    if len(str)==0:
        return str
    else:
        return str_rev(str[1:])+str[0]

print(str_rev(str))

menu=['espresso','mocha','latte','cappuccino','cortado','americano']

# outputs all elements which contains "s" char
def fin_coffe(coffee):
    if coffee[0]=='c':
        return coffee

# map_coffee=map(fin_coffe,menu)
# print(map_coffee)
#
# for x in map_coffee:
#     print(x)

filter_coffe=filter(fin_coffe,menu)
print(filter_coffe)

for x in filter_coffe:
    print(x)

data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)

