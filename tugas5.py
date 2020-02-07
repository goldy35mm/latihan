## Tugas 5 List
# Menu
#  1) Show Produk
#  2) Tambahkan Produk
#  3) Update Harga
#  4) Hapus Produk

# Pilih Menu nomor : 1 

# 1. Jeruk Rp. 1000
# 2. Apel Rp. 3000
# 3. Semangka Rp. 3000

# Balik kemenu awal?

# --------------------------------
# Menu 
#  1) Show Produk
#  2) Tambahkan Produk
#  3) Update Harga
#  4) Hapus Produk
# Pilih Menu nomor : 2 
# Nama produk yang akan ditambahkan : Mangga
# Harga produknya : 3000

# # ketika dipilih show produk 
# 1. Jeruk Rp. 1000
# 2. Apel Rp. 3000
# 3. Semangka Rp. 3000
# 4. Mangga Rp. 4000

# ---------------------------------
# Menu 
#  1) Show Produk
#  2) Tambahkan Produk
#  3) Update Harga
#  4) Hapus Produk
# Pilih Menu nomor : 3 
# 1. Jeruk Rp. 1000
# 2. Apel Rp. 3000
# 3. Semangka Rp. 3000
# 4. Mangga Rp. 4000

# Produk yang akan di update harganya : 4
# Harga Produk terbaru : 50000

# # ketika dipilih show produk 
# 1. Jeruk Rp. 1000
# 2. Apel Rp. 3000
# 3. Semangka Rp. 3000
# 4. Mangga Rp. 5000

# ---------------------------------------
# Menu 
#  1) Show Produk
#  2) Tambahkan Produk
#  3) Update Harga
#  4) Hapus Produk
# Pilih Menu nomor : 4 
# 1. Jeruk Rp. 1000
# 2. Apel Rp. 3000
# 3. Semangka Rp. 3000
# 4. Mangga Rp. 5000

# Produk yang akan dihapus : 2

# # ketika dipilih show produk 
# 1. Jeruk Rp. 1000
# 2. Semangka Rp. 3000
# 3. Mangga Rp. 5000

# menu = input('Pilih menu yang anda inginkan \n 1. Show produk \n 2. Tambahkan produk \n 3. update harga \n 4. hapus produk \n 5.exit \n Pilih menu nomor:')
# if(menu.isdigit()==True):
#             if(int(menu)>0 and int(menu)<=4):
#                 check=True
#             else:
                
#                 print("nomor salah, masukan pilihan 1-4")
# else:
#     print("nomor salah, masukan pilihan 1-4")
#     print("-----------------------------")

# if (menu == '1'):


def showproduk():
    print ("produk buah")
    for i in range(len(list_buah)):
            print(f'{i+1}. {list_buah[i][0]} rp.{list_buah[i][1]}')


def tambahkanproduk():
    tambah = input("tambahkan produk yang anda inginkan:")
    harga = input("tambahkan harga produk:")
    list_buah.append([tambah,int(harga)])
    print(f'buah yang ditambahkan{tambah},{harga}')
    
def updateharga():
    print('update harga')
    showproduk()
    update1 = input('yang ingin di update nomor berapa:')
    harga2 = int(input('harga yang ingin di update berapa:'))
    list_buah[int(update1)-1][1]=harga2
    print(f'buah yg diupdate{update1},harga yang di update{harga2}')

def hapusproduk():
    print('hapusproduk')
    showproduk()
    hapus1 = int(input("yang ingin dihapus nomor berapa:"))
    
    list_buah.pop(hapus1-1)

list_buah = [['semangka', 5000],['apel', 3000]]  

Exit = False
while Exit == False:
    print ("\n==================================")
    print ('SELAMAT DATANG DI APLIKASI INI')
    print ("==================================")


    menu = input('Pilih menu yang anda inginkan \n 1. Show produk \n 2. Tambahkan produk \n 3. update harga \n 4. hapus produk \n 5.exit \n Pilih menu nomor:')

    # else:
    #     print("nomor salah, masukan pilihan 1-5")
    #     print("-----------------------------")
    if (menu =='1'):
        showproduk()
    elif (menu == '2'):
        tambahkanproduk()
    elif (menu == '3'):
        updateharga()
    elif (menu == '4'):
        hapusproduk()
    elif (menu == '5'):
        print('')
        
    tanya = input("apakah mau keluar(ya/tidak) : ")
    if tanya =='ya':
        print("________________________________")
        print('Terimakasih sudah menggunakan aplikasi ini')
        print('_________________________________')
        Exit = True
        
        

    

