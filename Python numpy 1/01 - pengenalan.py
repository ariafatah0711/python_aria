import numpy as np

a = np.array([1,2,3,4,5,6])
b = [1,2,3,4,5,6]

print(f"array\t\t: {a}")
print(f"no array\t: {b}")

a = a+1 # saat di tambah dia akan menambahkan ke semua index
print(f"array\t\t: {a}") # contoh index pertama 1 lalu 2,3 dan seterusnya maka akan menjadi 2,3,4 

b = b+[1] # mengappend saja
print(f"no array\t: {b}") # hanya menambahkan angka di list tidak menambah ke semuanya