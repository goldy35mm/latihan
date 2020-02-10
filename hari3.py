
# usiaAndi = 40;

# usiaAndi *= 2;
# print(usiaAndi);
# usiaAndi /= 2;
# print(usiaAndi);
# usiaAndi += 2
# print(usiaAndi);
# usiaAndi -= 2
# print(usiaAndi);
# usiaAndi %= 2
# print(usiaAndi);


# ComparisonOperators

# x = 5;
# y = '5';

# print(x == y);
# print(x > int(y));
# print(x >= int(y));
# print(x < int(y));
# print(x <= int(y));

# Logical Operators

# x = 5;
# y = '5';
# z = 6;

# print(x==int(y) and int(y)<z);
# print(x==int(y) or int(y)<z);
# print(not(x==int(y) or int(y)<z));


# If, else if & else

# if (condition) :
# program;
# elif (condition) :
# program;
# else :
# program;

# If, else if & else

# nilai = 40;

# if (nilai > 80) :
# print('Excellent!');
# elif (nilai >= 60 and nilai <= 80) :
# print('Good job!');
# else :
# print("Don't give up!");

#solveit1

# perintah = int(input("masukan angka:")

# if perintah % 2 == 0 :
#     print(F"perintah {perintah} Tergolong bilangan genap")

# else :
#      print(F"perintah {perintah} Tergolong bilangan ganjil")

# a = 5
# a += 10
# print(a)

# nama = "goldy"
# nama += " fatihadi"
# print(nama)

#if elif else

# if(condition):
#     algoritma/program

# else(condition):
#     algoritma2

# nilai murid = 80

# if nilai_murid >= 70:

# IMT = massa(kg) / tinggi(meter)^2

# a. imt < 18.5 artinya berat badan kurang,
# b. 18.5 - 24.9 artinya berat badan ideal
# c. 25.0 - 29.9 artiya berat badan berlebih
# d. 30.0 - 39.9 artinya berat badan sangat berlebih
# e. IMT > 39.9 artinya obesitas

# massa = int(input("masukan massa(kg):"))
# tinggi = (input("masukan tinggi(m):"))
# tinggi = tinggi/100
# IMT = massa/tinggi**2

# if IMT <18.5:
#     print(IMT,"artinya berat badan anda kurang")

# elif IMT >=18.5 and <=24.9:
#     print("IMT", IMT, "artinya berat badan ideal ")


# massa = int(input("masukan massa(kg):"))
# tinggi = int(input("masukan tinggi(m):"))/100
# IMT = massa/tinggi**2
# hasil = "IMT anda adalah " + str(IMT) + " berat badan"

# if (IMT < 18.5):
#     hasil += " kurang"

# elif (18.5 <= IMT <25):
#     hasil += " ideal"

# elif (25.0 <= IMT <30):
#     hasil += " berlebih"

# elif (30 <= IMT <40):
#     hasil += " sangat berlebih"

# elif (IMT >= 40):
#     hasil += " umur anda pendek"

# print(hasil)

# menu = input ("Pilih menu yang anda inginkan \n 1.Home \n 2. About \n 3. Exit \n Pilih menu nomor:")

# if(menu.isdigit()==True):
#     if(int(menu)>0 and int(menu)<=3):
#         check=True
#     else:
#         print("input salah, masukan piliha 1-3")
#         print("-----------------------------")
# else:
#     print("input salah, masukan pilihan 1-3")
#     print("-----------------------------")

#loop

# angka = 1

# while(angka <= 10):
#     print(angka)
#     angka += 1

# #for loop and list

# listItem = list(range(1,11,2))
# print(listItem)

# for item in range(1,11,2):
#     print(item)

#loop drawing

#range(start,stop,step)

# y = 'Nomor urut '

# for item in range(0,21,2):
#     print(y + str(item)


# out = ""


# for item in list(range(5)):
#     out += ' * '
#     print(out)


# out = ""
# # x = 5

# for item in (range(5,0,-1)):
#     for item1 in range(0, item):
#         out += ' * '
#     print(out)

# Exit = 200
# while Exit == 200 :
#         menu = input('Pilih menu yang anda inginkan \n 1. Belajar \n 2. Belanja \n 3. Exit \n Pilih menu nomor:')

#         if (menu.isdigit()==True):
#                 if (int(menu) >0 and int (menu)<=3): # untuk menu
#                         Check = True
#                 if (int(menu) == 1): #untuk Belajar
#                         belajar = input("Pilih perhitungan \n 1. Luas segitiga \n 2. Luas trapesium \n Pilih nomor: ")
#                         if (int(belajar)>0 and int (belajar)<=1): #untuk luas segitiga
#                                 t = int(input("tinggi segitiga: "))
#                                 a = int(input("alas segitiga: "))
#                                 langkah = (a * t)*1/2
#                                 print("jadi luas segitiga adalah:",langkah)
#                         if (int(belajar)>1 and int(belajar)<=2): #untuk luas trapesium 
#                                 t = int(input("tinggi trapesium: "))
#                                 j = int(input("sisi sejajar trapesium: "))
#                                 langkah_t = (t*j+j)/2
#                                 print("jadi luas trapesium adalah:",langkah_t)

#                 if (int(menu) == 2): # untuk Belanja.
#                         belanja = input("pilih belanja apa \n 1. buah \n 2. daging \n Pilih nomor:")
#                         if (int(belanja)>0 and int(belanja)<=1): # untuk buah
#                                 buah = input("buah apa \n 1. salak \n 2. jambu \n Pilih buah nomor:")
#                                 if (int(buah)>0 and int(buah)<=1):
#                                         print("salak")
#                                 elif (int(buah)>1 and int(buah)<=2):
#                                         print("jambu")


#                         if (int(belanja)>1 and int(belanja)<=2): # untuk daging
#                                 daging = input("daging apa \n 1. Sapi \n 2. ayam \n Pilih daging nomor:")
#                                 if (int(daging)>0 and int(daging)<=1):
#                                         print("sapi")
#                                 elif (int(daging)>1 and int(daging)<=2):
#                                         print("ayam")

                                

#         if (int(menu) == 3): # untuk Exit
#                 Exit = 300
#                 print("Keluar dari program ")

