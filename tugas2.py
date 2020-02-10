# Pilih Menu 
# 1) Belajar
# 2) Belanja 
# 3) Exit

Exit = 200
while Exit == 200 :
        menu = input('Pilih menu yang anda inginkan \n 1. Belajar \n 2. Belanja \n 3. Exit \n Pilih menu nomor:')

        if (menu.isdigit()==True):
                if (int(menu) >0 and int (menu)<=3): # untuk menu
                        Check = True
                if (int(menu) == 1): #untuk Belajar
                        belajar = input("Pilih perhitungan \n 1. Luas segitiga \n 2. Luas trapesium \n Pilih nomor: ")
                        if (int(belajar)>0 and int (belajar)<=1): #untuk luas segitiga
                                t = int(input("tinggi segitiga: "))
                                a = int(input("alas segitiga: "))
                                langkah = (a * t)*1/2
                                print("jadi luas segitiga adalah:",langkah)
                        if (int(belajar)>1 and int(belajar)<=2): #untuk luas trapesium 
                                t = int(input("tinggi trapesium: "))
                                j = int(input("sisi sejajar trapesium: "))
                                langkah_t = (t*j+j)/2
                                print("jadi luas trapesium adalah:",langkah_t)

                if (int(menu) == 2): # untuk Belanja.
                        belanja = input("pilih belanja apa \n 1. buah \n 2. daging \n Pilih nomor:")
                        if (int(belanja)>0 and int(belanja)<=1): # untuk buah
                                buah = input("buah apa \n 1. salak \n 2. jambu \n Pilih buah nomor:")
                                if (int(buah)>0 and int(buah)<=1):
                                        print("salak")
                                elif (int(buah)>1 and int(buah)<=2):
                                        print("jambu")


                        if (int(belanja)>1 and int(belanja)<=2): # untuk daging
                                daging = input("daging apa \n 1. Sapi \n 2. ayam \n Pilih daging nomor:")
                                if (int(daging)>0 and int(daging)<=1):
                                        print("sapi")
                                elif (int(daging)>1 and int(daging)<=2):
                                        print("ayam")

                                

        if (int(menu) == 3): # untuk Exit
                Exit = 300
                print("Keluar dari program ")

