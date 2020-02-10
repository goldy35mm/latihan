
#untuk mencari hari
# import datetime

# d = datetime.date.today()

# print(d.day)

#Funtion for check name 
# def check_name(name,alphabet):

# def check_name(name,alphabet):
    # if alphabet in name:


# #test function
# check_name('Anugrah Nurhamid','A')
# # check_name('Arya Stark','A')



# def string_filter(text):

def string_filter(text):
    out = ""
    for tex in text:
        if tex.isnumeric() :
            out += tex
    return out
    

# # #test function 
print(string_filter('9Anya11'))
print(string_filter('11Pevita875'))
print(string_filter('W34AREM4NU'))






# #Function for check maximum number [DONE]
# def max_number(num1, num2, num3, num4):
#     numBesar = max(num1,num2,num3,num4)
#     return numBesar


# # #test function
# print(max_number(911,711,811,611))
# print(max_number(1289,1981,1995,1375))
# print(max_number(1890,1891,1888,1900))





#Function for validation plat number 

# def check_plat(platnomor):

# #test function
# check_plat('D 4444 CBR') -> Kendaraan anda dengan plat nomor sekian boleh lewat 
# check_plat('D 1576 ADT')
# check_plat('D 5959 RF')

