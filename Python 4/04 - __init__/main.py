import sains

# bisa jalan karena di init kita mengimport module matematika
''' from . import matematika ''' # dari init kembali ke sains lalu import matematika
''' from .import basic ''' # lalu dari init matematika kita mengimiport ke basic

# tambah
hasil_tambah = sains.matematika.basic.tambah(2,3,5,10)
print(f"hasil tambah: {hasil_tambah}")

# gaya
hasil_fisika = sains.fisika.gaya(2,5)
print(f"hasil gaya: {hasil_fisika}")

# kali
hasil_kali = sains.matematika.basic.kali(2,5)
print(f"hasil kali adalah {hasil_kali}")

# pangkat
hasil_pangkat = sains.matematika.science.pangkat(2)(5)
print(f"hasil pangkat: {hasil_pangkat}")

## atau

# from sains import * # kalau * untuk all

# # gaya
# hasil_fisika = fisika.gaya(2,5)
# print(f"hasil gaya: {hasil_fisika}")

# # kali
# hasil_kali = matematika.basic.kali(2,5)
# print(f"hasil kali adalah {hasil_kali}")

# # pangkat
# hasil_pangkat = matematika.science.pangkat(2)(5)
# print(f"hasil pangkat: {hasil_pangkat}")

## atau import lebih cepet
pangkat_3 = sains.matematika.pangkat(3)(2)
print(f"hasil pangkat 3 {pangkat_3}")