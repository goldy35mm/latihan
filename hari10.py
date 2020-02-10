# def check_name(name,alphabet):
#     if(alphabet.lower() in name or alphabet.upper() in name):
#         print('True')
#     else:
#         print('False')

# check_name("Goldy Fatihadi", 'G')

# def add_even(num):
#     if (num % 2 == 0):
#         print('angka ' + str(num) + 'Adalah angka genap')
#     else:
#         print('angka ' + str(num) + 'Adalah angka genap')

# add_even(1981)
# add_even(122)

# def string_filter(text):
#     filter_string = ''.join([i for i in text if i.isdigit()])#list comprehension
#     print(filter_string)

# string_filter('123Goldy78624')

# from datetime import date
# def check_plat(platnomor):
#     for i in platnomor:
#         if(i.isdigit()):
#             digit =int(i)
#     hari = date.today().day
#     if digit%2 == 0 :
#         digitakhir = 'Genap'
#     else:
#         digitakhir = 'Ganjil'
#     if hari % 2 == 0 :
#         hariini = 'Genap'
#     else:
#         hariini = 'Ganjil'
#     if digitakhir == hariini:
#         print('Hari ini tanggal ' + str(hari) + 'Plat nomer ini ' + str(platnomor) + ' diperbolehkan lewat' )
#     else:
#         print('Hari ini tanggal ' + str(hari) + 'Plat nomer ini ' + str(platnomor) + ' tidak diperbolehkan lewat' )

# check_plat('D 4444 CBR')
# check_plat('D 5761 CBR')


