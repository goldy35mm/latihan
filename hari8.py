# # import math

# # def reverseList(thelist):
# #     for i in range(0, math.floor(len(thelist)/3  )):
# #         templist = thelist[i]
# #         thelist[i] = thelist[len(thelist) -1 -i]
# #         thelist[len(thelist) -1 -i] = templist

# #     return thelist

# # print(reverseList([1,2,3,4,5,6,7,8]))

# #mode

# x = [ 1,2,3,2,5,2,7,2 ]
# def getMode(list) :
#     countList = []
# # create countList
#     for num in list :
#         check = False
#         for list1 in countList :
#             if(list1[0] == num) :
#                 list1[1] += 1
#                 check = True
#         if(check == False) :
#             countList.append([num, 0])

# # create list of mode/s
#     maxFrequency = 0
#     modes = []
#     for list1 in countList :
#         if (list1[1] > maxFrequency) :
#             modes = [list1[0]]
#             maxFrequency = list1[1]
#         elif (list1[1] == maxFrequency) :
#             modes.append(list1[0])

#     # if every value appears same amount of times
#     if (len(modes) == len(countList)) :
#         modes = []
#     return modes

# print(getMode(x))

#dictionary
#same as list but have key value
#{}


#   


# for key,value in x.items():
#     print(value)


# #tuple

# x = [1,2,3,4,5]
# y = [9,8,7,6,5]

# # for item in zip(x,y):
# #     print(item)

# print(x.values())
# print(x.key())

# lambda

# x = lambda a : a + 10
# print(x(5))

# x = lambda a,b : a * b
# print(x(5,10))

# x = lambda a,b,c : a+b+c
# print(x(5,5,5))

# def function(number):
#     return lambda a : a * number

# perkalian = function(2)

# print(perkalian(33))

# def lima():
#     return 5

# a = lambda x : x*lima()
# print(a(3))


# Map


# def add(n):
#     return n +n
# numbers = (1,2,3,4,5,)
# result = map(add,numbers)
# print(list(result))

# def times2(num) :
#     return num * 2
# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(map(times2, listNum))
# print(listNum)

# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(map(lambda num: num * 2, listNum))
# print(listNum)

# number1 = [1,2,3,4,5]
# number2 = [5,4,3,2,1]

# result = map(lambda  x,y : x +y, number1,number2)
# print(list(result))

# def duplicateMap(function,iteration):
#     for i in range(len(0,number1[1])):
#         for j in range(len(0,number2[1])):
#             function = i + j
#     return function


#  print(duplicateMap[1,2,3,4,5],[5,4,3,2,1])       
# number = [1,2,3,4,5]
# def duplicateMap(function,list_aja):
#     hasil = []
#     for item in list_aja:
#         hasil.append(function(item))
#     return hasil

# result =duplicateMap(lambda x: x +2,number)

# def pertambahan(n):
#     return n +2


# list_nama = ['goldy', 'maudy', 'dicky']



# def duplicatefilter(function,list_aja):
#     hasil = []
#     for item in list_aja:
#         if function(item):
#             hasil.append(item)
#     return hasil


# tahun = [1991,1992,1993,1994,1995]
# corona = duplicatefilter(lambda tahun: tahun % 2 == 0, tahun)
# print(list(corona))