# MODULE 1:
from tarfile import calc_chksums

# DJANGO (Web development) - YOUTUBE, INSTAGRAM....
# Variables
# encoding uni code for strings
# control flow, match statemenet comapres a value to serveral different conditions until one is met.
# looping: for vs. while
# looping enumrate through lists
# *controlling loop by break, continue and pass
# nested for loop


# functions
# scoping: local, enclosing, global, built-in scope LEGB
# built-in data strctures
# Mutable - inmmutable
# args & kwargs(keyword args)
# Error and exception
# try ~ except
# File handling ..


# birth_year=input('Enter your birth year:')
# age=2024-int(birth_year)

# https_status=500
#
# match https_status:
#     case 200|201:
#         print('Sucesss')
#     case 400:
#         print('Not Found')
#     case 500|501:
#         print('Server error')
#     case _:
#         print('unknown')


# for i in range(1,5):
#     print('*'*i)

# j=1
# while j<5:
#     print('*'*j)
#     j+=1
#
# lists=['2e3','333','32','22']
#
# for idx, item in enumerate(lists):
#     print('I like this number',f'{idx}:',item)

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', "Pudding", 'Churros', 'Tiramisú', 'Chocolate Cake']

# for idx, dessert in enumerate(favorites):
#     if dessert == 'Pudding':
#         print(f'Yes one of my favorite desserts is {idx}: ', dessert)
#         break
#     else:
#         print('No sorry, not a dessert on my list')

#Starter Code
# favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
#
# for dessert in favorites:
#     if dessert == 'Churros':
#         continue
#     print('Other desserts I like are', dessert)


# Starter Code
# favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
#
# for dessert in favorites:
#     if dessert == 'Churros':
#         pass
#     print('Other desserts I like are', dessert)

# for i in range(2): # col
#     for j in range(5): # row
#         print('*',end=' ')
#     print('')

#
# bill=175.000
#
# tax_rate=15
#
# total_tax=(bill*tax_rate)/100.00
#
# def caclulate_tax(bill, tax_rate):
#     return (bill*tax_rate)/100.00
#
# print(caclulate_tax(bill, tax_rate))
#
# # SCOPING
#
# my_global=10
#
# def fn1():
#     enclosed_v=8
#
#     def fn2():
#         local_v = 5
#         print('Access to Global', my_global)
#         print('Access to Enclosed', enclosed_v)
#     fn2()
# # print('cannot access to local', local_v)

# fn1()


# def sum_of(*args):
#     sum=0;
#     for x in args:
#         sum+=x
#     return sum
#
# print(sum_of(1,2,4))


# def sum_of(**kwargs):
#     sum=0;
#     for k,v in kwargs.items():
#         sum+=v
#     return round(sum,1)
#
# print(sum_of(coffee=2.99, cake=4.55))




# Starter code
# items = [1,2,3,4,5]
#
# try:
#     item = items[6]
# except Exception as e:
#     print('something went wrong',e)

# try:
#     with open('file_does_not_exist.txt', 'r') as file:
#         print(file.read())
# except:
#     print("Unable to locate file")


# try:
#     with open('file.txt', 'wb') as file:
#         print(file.write())
# except:
#     print("Unable to create a file")

# CREATE A FILE, INSERT CONTENT

with open('newfile.txt', 'w') as file:
    file.writelines(['this is a new file created', '\nthis is another file'])



