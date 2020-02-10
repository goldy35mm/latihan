# firstdict = {}

# def MenuDictionary(input):
#     #key | VALUE
#     print('|        key     |       value       |')
#     hasil = ''
#     i=0 #untuk nomor angka di depan
#     for key,value in input.items():
#         i+=1
#         hasil += f'{i}. {key}       {value}\n'
#     return hasil

# def ShowDictionary():
#     print(MenuDictionary(firstdict))

# def AddDictionary():
#     inputlooping = input('Berapa kali akan memasukan dictionary : ')
#     for i in range(int(inputlooping)):
#         print('Pilih tipe dictionary \n 1) String \n 2) Number ')
#         pilihdict = input('Pilih :')
#         if pilihdict == '1':
#             key = input('Key:')
#             value = input('Value: ')
#             firstdict[key.center(10)]=value.center(10)
#         elif pilihdict =='2':
#             key1 = input('Key:')
#             value1 = input('Value: ')
#             firstdict[key1.center(20)]=int(value1.center(20))
#             print()

# def searchdict():
#     search  = input('Kata yang anda cari: ')
#     filterdict = filter(lambda item: search.lower() in item.lower(), firstdict.keys())
#     newdic ={}
#     for item in filterdict:
#         newdic[item] = firstdict[item]
#     print(MenuDictionary(newdic))

# def outaplikasi():
#     print('Terimakasih sudah menggunakan aplikasi kami!')
#     exit()


#     backtomenu = input('Kembali ke awal y/n :')
#     print('')
#     print('Terimakasih sudah menggunakan layanan ini!')

#example python fundamental


# decision['testing'][2][1][1]['ada apa'][1][0]

# from math import floor, pow ,sqrt,ceil
# # a =[1,2,3,4,2,3,4,5,6,7,8,6,5,4,5,7,2,4,6,7,8,9,4,3]

# # duplicate mean
# def mean_list(list):
#     return sum(list)/len(list)

# def median_list(list):
#     list = bubble_sort(list)
#     if len(list)%2 == 0:
#         return ((list[(len(list)//2)-1]) + (list[(len(list)//2)]))/2
#     else:
#         return list[floor(len(list)/2)]



# def bubble_sort(list):
#     for i in range(len(list)-1,0,-1):
#         for j in range(i):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#     return list

# def mode_list(list):
#     ind = set(list)
#     counter ={}
#     modus = []
#     for i in ind:
#         z = 0
#         for j in list:
#             if i ==j:
#                 z += 1
#         counter[i] = z
#     max_count = max(counter.values())
#     for k in counter:
#         if counter[k] == max_count:
#             modus.append(k)
#     if len(modes) == len(set(list)):
#         modes = []
#     return modes


# def variance_lits(list):
#     z =0 
#     mean = mean_list(list)
#     for i in list:
#         z += pow((i - mean),2)
#     return z/(len(list)-1)

# def stdev(list):
#     z = 0
#     mean = mean_list(list)
#     for i in list :
#         z += pow((i -mean),2)
#     return sqrt(z/(len(list)-1))


# def sample_statistic(lits,type ='mean'):
#     if type == 'mean':
#         return mean_list(list)
#     elif type == 'stdev':
#         return stdev(lits)
#     elif type == 'median':
#         return median_list(list)
#     elif type == 'mode':
#         return mode_list(list)
#     elif type == 'variance':
#         return variance_lits(list)
#     else:
#         return 'Input tidak sesuai!'

# a =[1,2,3,4,2,3,4,5,6,7,8,6,5,4,5,7,2,4,6,7,8,9,4,3]
# print(sample_statistic(a,'mean'))
# print(sample_statistic(a,'stdev'))
# print(sample_statistic(a,'median'))
# print(sample_statistic(a,'mode'))
# print(sample_statistic(a,'variance'))


#get sqrt(292)
# output 4164

# def getSquare(num):
#     num1 = str(num)
#     g = ''
#     for i in list(num1):
#         g += str(int(pow(int(i),2)))
#     print(g)

# getSquare(242)


# s

# def domainName(cari):
#     cari =''
#     x = list(filter(lambda cari: cari == x, cari))
#     for x in cari:
#         return cari

# print(domainName(git))

# def domainName(cari):
    