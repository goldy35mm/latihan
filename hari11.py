# def remove_outlier(data):
#     datasorted = sorted(data)
#     mid = len(data)//2 #mengambil nilai tengah
#     data1 = datasorted[0:mid]
#     data3 = datasorted[-mid:]
#     q1 = data1[len(data1)//2]/2 if len(data1) % 2 != 0 else (data1[len(data1)//2] + data1[len(data1)//2 +1])/2
#     q3 = data3[len(data3)//2]/2 if len(data3) % 2 != 0 else (data3[len(data3)//2] + data3[len(data3)//2 -1])/2
#     IQR = q3 - q1
#     lower_limit = q1 - 1.5 *IQR
#     upper_limit = q3 + 1.5 *IQR

#     data_no_outlier = []
#     for item in data:
#         if item > lower_limit or item < upper_limit:
#             data_no_outlier.append(item)

#     print(f'Data asli adalah = {data}')
#     print(f'Data setelah di sort adalah = {datasorted}')
#     print(f'Setengah data pertama = {data1}')
#     print(f'Setengah data terakhir = {data3}')
#     print(f'Quartal satu adalah = {q1}')
#     print(f'Quartal dua adalah = {q3}')
#     print(f'Lower limitnya adalah = {lower_limit}')
#     print(f'upper limitnya adalah = {upper_limit}')
#     print(f'Data outliner adalah = {data_no_outlier}')

# remove_outlier([71, 70, 73, 70, 70, 69, 70, 72, 71, 300, 71, 69])

# #soal nomor 2
# def countVowel(data):
#     jumlahVowels = 0
#     vowels = ['a','i','u','e','o']
#     for item in data:
#         if(item.lower() in vowels):
#             jumlahVowels += 1
#     print(jumlahVowels)


# countVowel('BUdi Pergi Ke Pasar')

#soal nomor 3

# inputan = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]

# def given(array):
#     templist = []
#     for item in array:
#         for element in item:
#             templist.append(element)
#     templist.sort()
#     print(templist)# print bisa juga pakai return


# given([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]])       


#soalnomor 4

# def countWords(words):
#     wordlist = words.split(' ')
#     countWords1 = {}
#     for item in wordlist:
#         if (item in countWords1.keys()):
#             countWords1[item]+= 1
#         else:
#             countWords1[item]=1
#     for key,value in countWords1.items():
#         print(F'Jumlah kata '{key.capitalize()} ' ada sebanyak {value}')

# countWords('jangan jangan kamu adalah aku')