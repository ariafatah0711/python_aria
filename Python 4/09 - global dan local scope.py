# global dan local scope
# variable di loop dan if adalah variable local
#sedangkan function adalah variabke gkobal

nama_global = "otong"

## akses variable global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan nama {nama_global}")

fungsi1()

# akses variable dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# oercabangan
if True:
    print(f"menampilakan {nama_global}")

# intinya global hidup dimanapun

## variable local scope
def fungsi2():
    nama_local = "ucup" # variable local

fungsi2()
# print(nama_local) # tidak bisa di akses/error

## contoh 1: penggunaan
def say_otong():
    print(f"hello {nama}")

nama = "otong"
say_otong()

## contoh 2: merubah variable global
# global angka
angka = 0
nama = "ucup"

def ubah_angka(nilai_baru, nama_baru):
    global angka # fungsi ini mendapat akses merubah angka
    global nama
    angka = nilai_baru
    nama = "aria"

print(f"seblumnya {angka,nama}")
ubah_angka(10, "aria")
print(f"seblumnya {angka,nama}")

## contoh 3:
angka = 0
for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka_dummy = 100
    angka = 0

print(angka_dummy)