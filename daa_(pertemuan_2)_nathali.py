# -*- coding: utf-8 -*-
"""DAA (Pertemuan 2) - Nathali

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VjBPkFVxf9PC5YUzqbnCpZtnDfdqeHN0
"""

#Latihan 1
import numpy as np
nilai_siswa = np.array([85, 55, 40, 90])
print(nilai_siswa[3])

#Latihan 2
print("Hello World!")
print("Nama saya Nathali Katrin")
print("NIM saya 2023071016")

#Latihan 3
if 5 > 2:
    print("Five is greater than two!")

#Latihan 4
x = 5
y = "John"
print(x)
print(y)

#Latihan 5
x = 4
x = "Sally"
print(x)

#Latihan 6
mylist = [1,2,3,4]

getFirst = mylist[0]
getSecond = mylist[1]

print(getFirst)
print(getSecond)

#Latihan 7
mylist = [1,2,3,4]

getFirst = mylist[0]
getLast = mylist[4]

print(getFirst)
print(getLast)

#Latihan 8
mylist = [1,2,3,4]

getKali = 1
for num in mylist:
    getKali *= num

print(getKali)

#Latihan 9
mylist = [1,2,3,4]

getBagi = 1
for num in mylist:
    getBagi /= num

print(getBagi)

#Latihan 10
hm1 = [1,2,3,4,5]
hm2 = [1,2,3]

getSum1 = 0
for num in hm1:
    getSum1 += num

getSum2 = 0
for num in hm2:
    getSum2 += num

print(getSum1/getSum2)

#Latihan 11
hm1 = [1,2,3,4,5]
hm2 = [1,2,3]

getSum1 = 0
for num in hm1:
    getSum1 += num

getSum2 = 0
for num in hm2:
    getSum2 += num

print(getSum1-getSum2)