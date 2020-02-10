# produk =["Jeruk","Semangka","Mangga"]
# harga = [2000,5000,10000]

# def printMenu():
#     hasil = ''
#     for item in range(len(produk)):
#         hasil += str(item+1) + "." + produk[item] + ' Rp ' + str(harga[item]) + '\n'
#     return hasil

# def Showproduk():
#     print(printMenu())

# def inputData():
#     newProd = input('masukan produk:')
#     newPrice = int(input('Masukan harga produk dari {} '.format(newProd)))#int(input(f'Masukan harga {newProd}:))
#     produk.append(newProd)
#     harga.append(newPrice)
#     print('Produk berhasil ditambahkan !\n' + printMenu())

# def updateHarga():
#     pilihProd = input('Masukan produk yang akan di update \n' + printMenu() + '\n Pilih salah satu: ')
#     pilih = int(pilihProd)
#     newHarga = int(input('Harga' + produk[pilih] + 'akan dirubah berapa harganya:'))
#     harga[pilih] = newHarga
#     print('Harga produk berhasil dirubah !\n' + printMenu())

# def deleteProduk():
#     hapusProd = input('Pilih produk yang akan dihapus \n' +printMenu() + '\n Pilih salah satu : ')
#     index = int(hapusProd)-2
#     produk.pop(index)
#     harga.pop(index)
#     print('Produk berhasil dihapus ! \n ' + printMenu())

# kembaliKeMenu = False
# while (kembaliKeMenu==False):
    
#     pilihMenu = input('Pilih Menu \n 1) Show produk \n 2) Add produk \n 3) Update Harga \n 4) Delete Produk \n Pilih Salah satu: ')
#     index = int(pilihMenu)-1
#     menu = [Showproduk, inputData, updateHarga, deleteProduk]
#     menu[index]()
#     minta_keluar = input('Mau ke menu awal atau tidak? (y/n) :')
#     if minta_keluar == 'n':
#         print('Terimakasih telah menggunakan aplikasi ini')
#         kembaliKeMenu == True

#     else :
#         kembaliKeMenu == False

# def Hello():
#     print('Hello')

# def function():
#     return[1,2,Hello]

# function()[2]()# fungsi execute index execute

#print tidak memiliki value karena langsung execute print
# return menghasilkan sebuah value dimana value tersebut dapat diambil atau dipanggil kapanpun.
#yg penting di list
#- cara mengambil dari sebuah list, cara mengganti list, setelah diganti lalu di ambil dalam sebuah list

#Matrix dua dimensi
# produk = [
#     ['Jeruk', 2000],
#     ['Apel', 3000],
#     ['Pear', 4000]
# ]

# print(produk[2][1])

# cart =[
#     [0,3],
#     [1,4],
#     [2,5]
# ]



# out = ""
# for item in range(len(cart)):
#     index = cart[item][0]
#     out += str(item+1) + "." + produk[index][0] + 'Rp. '+ str(produk[index][1]) + 'x ' + str(cart[item][1]) + '=  rp. ' + str(produk[index][1]*cart[item][1] +'\n'

# print(out)

#Dictionary
#{}, changeaable, indexing,indexed
#key, value

# nama = {
#     'depan' : "Muchamad",
#     'Belakang' : 'Goldy'
# }

# # print(nama['depan'])
# # print(nama['Belakang'])

# nama['depan'] ='mad'
# print(nama['depan'])

#Tuple
#Unchangeable
# variable_tuple = {1,2,3,4,5,6,9,8}

# # print(type(variable_tuple))# untuk mencari tipe variabel

# a =('goldy', [1, True], {'nama' : 'Goldy'})

# print(a[1][1])#menghasilkan True
# a[1][1] = False #Tuple inde 1 sebuah list, index pertama dari list adalah True diganti dengan False
# a[1].append('False')
# print(a)


#Sets
#unique

# ini_set = {'apel','jeruk','mangga'}
# print(type(ini_set))

# for item in ini_set:
#     print(item)

#list comprehension
# list_num = [1,2,3,4,5]
# list_num = [item* 2 for item in list_num]
# print(list_num)


# def perkalian(num):
#     return num*2     

# list_num = [1,2,3,4,5]     
# list_num = [perkalian(item) for item in list_num]
# print(list_num)   

#lambda
# def perkalian(number):
#     return number * 2

# x = lambda number: number*2

# print(x[5])

# x = lambda a,b : a * b
# print(x(3,4))

#lambda di dalam function

# def function(n):
#     return lambda a: a * n

# dikali2 = function(2)

# print(dikali2(11))