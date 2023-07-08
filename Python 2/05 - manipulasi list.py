# List

# kumpulan data number
data_angka = [1, 2, 3, 4, 5]
print(data_angka),

# kumpulan data string
data_string = ["aria", "fatah", "anom"]
print(data_string)

# kumpulan data bool
data_bool = [True, False]
print(data_bool)

# kumpulan data campuran
data_campuran = [1, "aria", True]
print(data_campuran)

# cara alternatif membuat list 
data_range = range(0,10,2)
print(data_range)
data_list = list(data_range)
print(data_list)

# alternatif list for loop, list comprensif
data_list_for = [i*2 for i in range(0, 10)]
print(data_list_for)

# membuat list for idan if
list_list_campuran = [i for i in range(0, 10) if i != 5]
print(list_list_campuran)

# genap
list_list_campuran = [i for i in range(0, 10) if i % 2 == 0]
print(list_list_campuran)

# ganjil
list_list_campuran = [i for i in range(0, 10) if i % 2 != 0]
print(list_list_campuran)

###########################################################

# operasi 

#index = 0(-3)  1(-2)     2(-1)
data = ["ucup", "otong", "aria"]

# mengambil data dari list
data_0 = data[0]
print("data pertama: ", data_0)

data_terakhir = data[-1]
print("data terakhir: ", data_terakhir)

data_0 = data[-3]
print("data pertama: ", data_0)

# mengambil info panjang data
panjang_data = len(data)
print(f"panjang data: {panjang_data}")

# manipulasi data list

# menambahkan data list
print(f"data sebelum ditambah: {data}")

# variable.insert(posisi, value)
data.insert(1, "asep")
print(f"data sesudah ditambah: {data}")

# menambah di akhir list 

# variable.append(value)
data.append("zaki")
print(f"data ditambah di akhir: {data}")

# menggabungkan list dengan list 
data_baru = ["anjing, gugug"]

# variable.extand(value)
data.extend(data_baru)
print(f"data gabungan: {data}")

# merubah data 
# ke 2 jadi michal

print("sebelum diubah: ", data)
data[2] = "michal" 
print("setelah diubah: ", data)

# menghilangkan data

data.remove("aria")
print("remove aria: ", data)

# meremove data belakang

data.pop()
print("data paling terakhir di remove: ", data)

data.pop(1)
print("data kedua di remove: ", data)

# mengambil data akhir
data_akhir = data.pop()
print("data paling terakhir di ambil: ", data_akhir)

# delete data sebelum akhir atau sebeleum data terakhir
del data[-1]
print(data)