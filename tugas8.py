#Soal nomor 1
data = [71, 70, 73, 70, 70, 69, 70, 72, 71, 300, 71, 69]

# def sort_data(data): DONE
#     for i in range(len(data)):
#         for j in range(i+1, len(data)):
#             if data[i] > data[j]:
#                 data[i], data[j] = data[j], data[i]
#     return data

# print(sort_data([71, 70, 73, 70, 70, 69, 70, 72, 71, 300, 71, 69]))


def sortascending(data):
    for item in data:
        ascending = sorted(data)
    return ascending

# print(sortascending([71, 70, 73, 70, 70, 69, 70, 72, 71, 300, 71, 69]))

z = sortascending(data)


# if len(z)%2 == 0:
#     median = (z[len(z)//2] + z[len(z)//2-1])/2
# else:
#     median = z[len(z)//2]

# print(median)


def cari_median(z):
    if len(z)%2 == 0:
        median = (z[len(z)//2] + z[len(z)//2-1])/2
    else:
        median = z[len(z)//2]
    return median

quartal = cari_median(z)

# print(z)


def quartal1(z):
    if  len(z)%2 ==0:
        q1 = (z[len(z)//4] + z[len(z)//4-1])/2
    else:
        q1 = z[len(z)//4]
    return q1

def quartal3(z):
    if len(z)%2 == 0:
        q3 = (z[-(len(z)//4)] + z[-(len(z)//4+1)])/2
    else:
        q3 = z[-(len(z)//4)]
    return q3

IQR = quartal3(z) - quartal1(z)

# print(IQR)


def lowerlimit(z):
    lowlimit = quartal1(z)-1.5*IQR
    return lowlimit

# print(lowerlimit(z))
    
def upperlimit(z):
    uplimit = quartal3(z)+ 1.5*IQR
    return uplimit

# print(upperlimit(z))

def remove_outliner(z):
    for item in z:
        if item < lowerlimit(z)  or item > upperlimit(z):
            z.remove(item)
            return z
    

print(remove_outliner(z))



# Soal nomor 2 DONE
# count = 0 
# Kata = input("Masukan kata untuk hitung vowel").lower()
# for vowel in Kata:

#     if vowel in 'aeiou':

#         count += 1

# print(count)

# def hitung_vowel(kata): #still none
#     count = 0
#     for vowel in kata.lower():
#         if vowel in "aiueo":
#             count += 1
#     return vowel
        


# print(hitung_vowel('Goldy Fatihadi'))


#soal nomor 3 DONE

# list1  = [3,2,1]
# list2 = [4,5,6]
# list3 = [10,8,9,1]

# total = list1 + list2 +list3

# print(sorted(total))

# abcd = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
# def flattened_list(total):
#     x = []   
#     for item in total:
#         x += item
#     x.sort()
#     return x

# print(flattened_list(abcd))


#nomor 4

# words = "jangan jangan kamu adalah aku"

# kata = input('Masukan kata yang ingin dicari untuk diketahui jumlah : ')
# x= words.split()
# b = 0
# for item in x:
#     kata.count(x)
#     item += 1 
#     break
# print(item)



def word_calculate(kata):
    counts1 = dict()
    words = kata.split()

    for word in words:
        if word in counts1:
            counts1[word] += 1
        else:
            counts1[word] = 1
    return counts1

print(word_calculate('jangan jangan kamu adalah aku'))
            

