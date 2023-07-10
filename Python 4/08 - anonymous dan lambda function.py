# labda function

def f_kuadrat(angka):
    return angka**2

print("hasil fungsi kuadrat" ,f_kuadrat(4))

# kita coba dengan lambda
# output = lambda argumrnt: expression
kuadrat = lambda angka:angka**2
print("hasil fungsi kuadrat dengan lambda" ,kuadrat(5))

# dengan 2 input 
pangkat = lambda num,pow : num**pow
print(f"hasil pangkat dengan lambda {pangkat(10,2)}")

## kegunaanya

data_list = ["ucup","aria fatah","dudung"]

# shorting untuk list biasa
data_list.sort()
print(f"data sort: {data_list}")

# shorting dia pake panjang
data_list.sort(key=len) # panjang
print(f"data sort dengan len: {data_list}")

# sort tanpa lambda
def panjang_nama(nama):
    return len(nama)

# sort pakai lambda
data_list = ["ucup","aria fatah","dudung"]
data_list.sort(key=lambda nama : len(nama))
print(f"data sort dengan lambda: {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(data_angka_baru)

data_angka_baru = list(filter(lambda x : x<5,data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x : (x%2==0), data_angka)) # x module 2 artinya sisa bagi dari angka/2
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x : (x%2==1), data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x : x%3==0, data_angka))

# anonymous function
# currying <- haskell curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print("fungsi biasa:", data_hasil)

# dengan currying  menjadi
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2: {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat 3: {pangkat3(5)}")

# jika ingin langusung
print(f"pangkat bebas: {pangkat(2)(5)}") #pangkat(n)(lambda) = pangkat(2)(5)