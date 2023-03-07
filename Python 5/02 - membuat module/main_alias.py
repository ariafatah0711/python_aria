# modul matematika dengan import dengan alias

# alias untuk ganti nama agar lebih cpt
from matematika import tambah as ditambah
from matematika import kali as dikali
from matematika import pangkat as pangkat2

hasil_tambah = ditambah(1,2,3,4)
print(f"hasil tambah: {hasil_tambah}")

hasil_kali = dikali(6,6)
print(f"hasil kali: {hasil_kali}")

pangkat_2 = pangkat2(2)(5)
print(f"hasil pangkat: {pangkat_2}")

## ganti nama importnya
import matematika as math # artinya matematika menjadi math

# contoh
hasil_tambah = math.tambah(2,8) # lebih singkat dripda harus matematika.tambah(2,8)
print(f"hasil tambah: {hasil_tambah}")