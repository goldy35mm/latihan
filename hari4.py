
# Function

# def contoh():
#     print('Halo Dunia!')

# contoh()

# Function

# x = 10
# y = 50

# def contoh() :
#     print(x+y)

# contoh()

# Function with a Parameter

# def namaku(nama) :
#     print(nama + ' Susilo')

# namaku('Adi')
# namaku('Budi')
# namaku('Caca')
# namaku('Dedi')

# Function with 2 Parameters

# def data(x,y) :
#     print(x+' Lahir th '+y)

# data('Adi','1990')
# data('Budi','1991')
# data('Caca','1992')
# data('Dedi','1993')

#looping

# z =''
# for item in range(5):
#      for item1 in range(0, item+1):
#         z += ' * '
#      z += '\n'
# print(z)  
# for item in range(-5,0):
#      for item1 in range(0, item+1):
#         z += ' * '
#      z += ''

# print(z)  

# for i (5,-5,-1)

# z =''
# for i in range(5,0,-1):
#      if (i >1):
#          for j in range (0, i):
#             z += ' * '
#             z += '\n'
#      elif i == 1:
#         for k in range (0, 5,8):
#             for l in range (0,k+1):
#                 z += ' * '
#             if k == 4:
#                 break
#             z += '\n'
# print(z)  

# z =''
# for item in range(5):
#      for item1 in range(0, item+1):
#         z += ' * '
#      z += '\n'
# # for item in range(-5,0):
# #      for item1 in range(0, item+1):
# #         z += ' * '
# #      z += ''
#      print(z)


# for x in range (0,10):
#     print('     '*(10-x-1)+ "*" * (x*9+1))

# for x in range (-9,10):
#  print('    '*(10-x-1)+ "*" * (x*9+1))
# else: 
#     print('    '*(-10-x-1)+ "*" * (x*-9+1))
    
# k = 10
# for i in range(0, 10):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i+1):
#         print("* ", end="")
#     print() 


# # Latihan tambahan
# size = int(input("size yang diinginkan:")

# for i in range(0, 10):
#      for j in range(0, size):
#         print(end=" ")
#     k = size - 1
#      for j in range(0, i+1):
#         print("* ", end="")
#         print()    


# rows = input("masukan angka: ")
# rows = int (rows)

# for i in range (rows,0,-1):
#     for j in range(0, i + 1):
#         print("*", end=' ')

#     print("\r")

# size = input ('masukan angka:')
# for i in range (int(size)):
#     for j in range ((int(size)-i)-1):
#         print(end = " ")
#     for j in range(i+1):
#         print('*', end =" ")
#     print()
    
# b = input("masukan angka ")
# b = int (b)

# b = 10
# for i in range (b,0,-1):
#     for j in range(10 ):
#         print(j, end=' ')

#     print(" ")

# angka = int(input("masukan angka :"))
# c = 0
# for x in range(0, angka):
#     for y in range(1,x):
#         print(c, end=" ")
#         c = 3**(x+1)
#     print()

#untuk segitiga sama kaki 
# size = input ('masukan angka:')
# for i in range (int(size)):
#     for j in range ((int(size)-i)-1):
#         print(end = " ")
#     for j in range(i+1):
#         print('*', end =" ")
#     print()

# segitiga siku siku
# size = input("masukan angka: ")
# size = int (size)

# for i in range (0, size):
#     for j in range(0, i + 1):
#         print("*", end=' ')

#     print("")

# size = input("masukan size persegi:")
# size = int (size)

# for i in range (size): 
#     for i in range (size):
#         print("*",end=" ")
#     print()
               
Keluar = False
while(Keluar ==False):

    check = False
    while(check==False):
        #menu program
        menu = input('Pilih menu yang anda inginkan \n 1. Segitiga siku-siku \n 2. Segitiga sama kaki \n 3. Persegi \n Pilih menu nomor:')
        if(menu.isdigit()==True):
            if(int(menu)>0 and int(menu)<=3):
                check=True
            else:
                
                print("-----------------------------")
        else:
            print("nomor salah, masukan pilihan 1-3")
            print("-----------------------------")
    #segitiga siki-siku
    if(menu=='1'):
        check = False
        while(check==False):
            size = input("masukan size angka: ")
            size = int (size)
            for i in range(0,size):
                for j in range(0,i +1):
                    print("*",end="\n\n\n")
                print()
                check=True  
            else:
                print('___________________')

        # untuk stop looping
        check=False
        while(check==False):
            menu_2 = input('Apakah anda ingin kembali ke \n 1.Menu Awal \n 2.Exit \n Pilih Menu nomor : ')
            if(menu_2.isdigit()==True):
                if(int(int(menu_2)>0 and int(menu_2)<3)):
                    check = True
                else:
                    print('input salah, masukan 1 atau 2 ')
                    print('-----------------------------------')
            else:
                print('input salah, masukan 1 atau 2 ')
                print('-----------------------------------')
            
            if(menu_2=='2'):
                Keluar = True 
    
    if(menu =='2'):
        check = False
        while(check == False):
            size = input ('masukan size segitiga sama kaki:')
            for i in range (int(size)):
                for j in range ((int(size)-i)-1):
                    print(end = " ")
                for j in range(i+1):
                    print('*', end =" ")
                print("")
                check = True
            else:
                print("_________________________")
                
        # untuk stop looping
        check=False
        while(check==False):
            menu_2 = input('Apakah anda ingin kembali ke \n 1.Menu Awal \n 2.Exit \n Pilih Menu nomor : ')
            if(menu_2.isdigit()==True):
                if(int(int(menu_2)>0 and int(menu_2)<3)):
                    check = True
                else:
                    print('input salah, masukan 1 atau 2 ')
                    print('-----------------------------------')
            else:
                print('input salah, masukan 1 atau 2 ')
                print('-----------------------------------')
            
        if(menu_2=='2'):
            Keluar=True 
            
        
    if(menu=='3'):
        check=False
        while(check==False):
            size = input("masukan size persegi:")
            size = int (size)
            for i in range (size): 
                for i in range (size):
                    print("*",end=" ")
                print()
                check=True
            else:
                print("_______________________")
                print("-----------------------------")
        else:
            
            print("-----------------------------")
        # untuk stop looping
        check=False
        while(check==False):
            menu_2 = input('Apakah anda ingin kembali ke \n 1.Menu Awal \n 2.Exit \n Pilih Menu nomor : ')
            if(menu_2.isdigit()==True):
                if(int(int(menu_2)>0 and int(menu_2)<3)):
                    check = True
                else:
                    print('input salah, masukan 1 atau 2 ')
                    print('-----------------------------------')
            else:
                print('input salah, masukan 1 atau 2 ')
                print('-----------------------------------')
        if(menu_2=='2'):
                Keluar=True 

else:
    Keluar=True 
print("Terimakasih")