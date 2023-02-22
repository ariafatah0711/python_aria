# list didalam list

data_0 = [1, 2]
data_1 = [3, 4]

data_list_biasa = [1, 2, 3, 4]
print(f"data list biasa: {data_list_biasa}")

list_2d = [data_0, data_1]
print(f"data list_2d: {list_2d}")

# contoh penggunaan

peserta_0 =["ucup", 25, "laki laki"]
peserta_1 =["otong", 10, "laki laki"]
peserta_2 =["dedeh", 50, "wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]

print(f"\nlist peserta: {list_peserta}")

for peserta in list_peserta:
    print(f"nama: {peserta[0]}")
    print(f"umur: {peserta[1]}")
    print(f"gender: {peserta[2]}\n")

# dengan reference

list_copy = list_peserta.copy()
print(f"peserta: {list_copy}")

peserta_0[0] = "micheal"
print(f"\nlist peserta: {list_peserta}")
print(f"peserta: {list_copy}\n")

# Deep copy list

data_0 = [1, 2]
data_1 = [3, 4]

data_2d = [data_0, data_1, 10]
data_2d_copy = data_2d.copy()

print(f"data: {data_2d}")
print(f"data copy: {data_2d_copy}\n")

# mengambil data dari nested list
# data pertama
data = data_2d[0]
print("data", data)

# data pertama index 0
data = data_2d[0][0]
print("data", data)

# addres data 2d
print(f"\naddres asli: {hex(id(data_2d))}")
print(f"addres copy: {hex(id(data_2d_copy))}")

print("\naddres dari member ke 1")
print(f"addres asli: {hex(id(data_2d[0]))}")
print(f"addres copy: {hex(id(data_2d_copy[0]))}")

data_2d[1][0] = 5
data_2d[2] = 9

print(f"data: {data_2d}")
print(f"data copy: {data_2d_copy}\n")

### kita gunakan deep copy
from copy import deepcopy

data_2d = [data_0, data_1, 10]
# data_2d_copy = data_2d.copy()
# menjadiiii 
data_2d_deep = deepcopy(data_2d)

# addres data 2d
print(f"\naddres asli: {hex(id(data_2d))}")
print(f"addres copy: {hex(id(data_2d_copy))}")

data_2d[1][0] = 100
data_2d[0][0] = 50

print(f"\ndata: {data_2d}")
print(f"data copy: {data_2d_copy}")
print(f"\ndata deep copy: {data_2d_deep}")