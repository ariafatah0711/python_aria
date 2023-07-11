# modul matematika dengan from

from matematika import tambah, kali # artinya dari matematika kita mengimport tambah, kali
from matematika import * # arrtinya semuanya diambil

hasil_tambah = tambah(1,2,3,4)
print(f"hasil tambah: {hasil_tambah}")

hasil_kali = kali(6,6)
print(f"hasil kali: {hasil_kali}")

pangkat_2 = pangkat(2)(5)
print(f"hasil pangkat: {pangkat_2}")