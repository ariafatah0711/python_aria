# numpy | PIP
import numpy as np

list_a = [1,2,3,4]
# matrix a
vector_a = np.array([1,2,3,4])

# biasa
print(list_a)
print(f"list_a: {list_a}") # list biasa menggunakan koma
'''print(list_a**2)''' # error

# array
print(vector_a)
print(f"vector_a: {vector_a}") # list array tanpa koma
print(vector_a**2) # semua angka akan di kuadratkan

print("vector_a * 2: ",vector_a*2) # array akan mengalikan setiap angka
print("list_a * 2: ",list_a*2) # list biasa akan menduplicat list jadi 2 / di print 2X

# matrix b
matrix_b = np.array([(1,2),(3,4)])
print(f"matrix_b: \n{matrix_b}")
print(f"matrix_b ** 2: \n{matrix_b**2}") # semua angka di kuadratkan

# zeros c
zeros_c = np.zeros((2,2)) # artinya 2 angka dikali 2 angka jadinya keluar 0,0  0,0
print(f"zeros_c: \n{zeros_c}")

# ones d
ones_d = np.ones((2,2)) # sama seperti zero namun angkanya berubah menjadi satu karena ones
print(f"ones_d: \n{ones_d}")

#
jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah matrix b + matrix b**2 + ones d: \n{jumlah}")