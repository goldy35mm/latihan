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
        print('a')
        
    tanya = input("apakah mau keluar(ya/tidak) : ")
    if tanya =='ya':
        Exit = True
        
        

    




