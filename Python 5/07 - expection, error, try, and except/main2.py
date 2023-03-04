# contoh membuat exception

from numbers import Number
def tambah(a,b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise f"input pertama harus angka"
    return a + b

print(tambah(5, 7))

# menangkap dengan type exceptnya
angka = "a"
# bisa juga ubah ini menjadi apapun
try:
    hasil = 10/angka
except Exception as error_message:
    print(f"hasil dari 10/{angka} tidak berhasil karena") 
    print(error_message)

# bisa juga langsung ambil
try:
    angka = int(input("masukan angka dan bukan string: "))
    hasil = 10/angka
    print(angka)
except ValueError as error_message:
    print(error_message)
except ZeroDivisionError as error_message:
    print(error_message)

# ketika kita menulis 0 itu akan terdefinisi zero devision
# namun ketika angkanya kita tulis 0 itu terdefinisi literal atau value error