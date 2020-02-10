
# Pilihan 1
# Pilih Menu.
#  1) Menu Dictionary
#  2) Add Dictionary
#  3) Search Dictionary
#  4) Exit
# Pilih Menu : 1
# |    key    |    value    |

# Kembali Ke Menu Awal (y/n) : y
# -----------------------------------------------------------------
# # Pilihan 2
# Pilih Menu.
#  1) Menu Dictionary
#  2) Add Dictionary
#  3) Search Dictionary
#  4) Exit
# Pilih Menu : 2
# Berapa kali masukan dictionary : 2
# Pilih tipe Dictionary.
#  1) string
#  2) number
# Pilih : 1
# Key : Nama
# Value : Anugrah

# Pilih tipe Dictionary.
#  1) string
#  2) number
# Pilih : 1
# Key : Nama2
# Value : Anya

# Kembali Ke Menu Awal (y/n) : y
# --------------------------------------------------------------
# # Check apakah dictionary sudah masuk atau belum
# Pilih Menu.
#  1) Menu Dictionary
#  2) Add Dictionary
#  3) Search Dictionary
#  4) Exit
# Pilih Menu : 1
# |    key    |    value    |
# 1. Nama         Anugrah
# 2. Nama2          Anya

# Kembali Ke Menu Awal (y/n) : y
# --------------------------------------------------------------
# # Pilih menu 3
# Pilih Menu.
#  1) Menu Dictionary
#  2) Add Dictionary
#  3) Search Dictionary
#  4) Exit
# Pilih Menu : 3
# Cari kata : Nama2
# |    key    |    value    |
# 1. Nama2          Anya

# Kembali Ke Menu Awal (y/n) : n

# Terimakasih telah menggunakan aplikasi sederhana ini!

# menuDict = {
#     'nama' : 'goldy',
#     'nama2': 'maudy'
# }


# def MenuDictionary():
#     a = "key"
#     b = "value"
#     print('+' + a.center(23,' ') + '+' + b.center(23,' ') + '+')


#     for key,value in menuDict.items():
#         print(f'| {key.center(20)} |  {value.center(20)}  |')


# def AddDictionary():
 
#     jumlah = int(input('Ingin berapa yang ditambahkan :'))
#     i = 0
#     while i < jumlah:
#         key =input('Masukan Key Nama: ')
#         Val = input('Masukan Value: ')
#         menuDict[key] = Val
#         i += 1


# def SearchDictionary():
#     search = input('Kata yang ingin anda cari :')
#     cari = list(filter(lambda x: search == x, menuDict))
#     for i in cari:
#         print(f'| {i.center(20)} |  {menuDict[i].center(20)}  |')






# Exit = False
# while Exit == False:
#     print ("\n==================================")
#     print ('SELAMAT DATANG DI APLIKASI INI')
#     print ("====================================")

#     menu = input('Pilih Menu \n 1) Menu Dictionary \n 2) Add Dictionary \n 3) Search Dictionary \n 4) Exit \n Pilih nomor yang anda pilih? :')

#     if (menu == '1'):
#         MenuDictionary()
#     elif (menu == '2'):
#         AddDictionary()
#     elif (menu == '3'):
#         SearchDictionary()
#     elif (menu == '4'):
#         print('   | |   ')
#         print('  \   /  ')
#         print('   \ /   ')
#         print('    v    ')


#     tanya = input("apakah mau keluar(ya/tidak) : ")
#     if tanya =='ya':
#         print("__________________________________________")
#         print('Terimakasih sudah menggunakan aplikasi ini')
#         print('__________________________________________')
#         Exit = True
    

#first




