
# pilihan menu
# 1. Segitiga siku-siku
# 2. Segitiga sama kaki
# 3. Persegi
# pilih menu 1-3:
# # apakah akan ke menu awal

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