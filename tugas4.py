# Nomor 1

# def duplicate_string(parameter):
# 	# Write your code 

# # Run program 
# duplicate_string(anugrah) -> annuuuggggrrrrraaaaaahhhhhhh
# duplicate_string(grizly) -> grriiizzzzlllllyyyyyy

# def duplicate_string():
#     nama = input("Masukan Nama untuk duplicate:")
#     x = ""
#     for i in range(0,len(nama)):    
#         for j in range(0,i+1):
#             x += nama[i]
#     print(x)
# duplicate_string()


# s = 's'
# b = 'b'
# print(s+b)

# # Nomor 2
# def duplicate_string_strip(parameter):
#     # Write your code 

# # Run Program
# duplicate_string_strip(anya) -> -A-Nn-Yyy-Aaaa
# duplicate_string_strip(anugrah) -> -A-Nn-Uuu-Gggg-Rrrrr-Aaaaaa-Hhhhhhh

# def duplicate_string_strip():
#     x = ""
#     nama = input("masukan nama untuk duplicate strip")
#     for i in range(0, len(nama)):
#         x += "-"
#         for j in range(0,i+1):
#             if j == 0:
#                 x += nama[i].upper()
#             else :
#                 x+= nama[i].lower()    
        
#     print(x)       

# duplicate_string_strip()
# Nomor 3

# #Fungsi sort descending dan ascending

# def fungsi_sort_ascending(parameter):
# 	parameter.sort()
#     print(parameter)
#     # return parameter
    
# def fungsi_sort_descending(parameter):
# 	parameter.sort(reverse = True)

#     # return parameter
# # # Run Program
# print(fungsi_sort_ascending([1,10,2,6,1,2,5,6,10]))
# print(fungsi_sort_descending([1,10,2,6,1,2,5,6,10]))

def total(x,y):
    z = x+y
    return z

print(total(4,5))
print()



