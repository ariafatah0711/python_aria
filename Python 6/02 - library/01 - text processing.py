# string => adalah module bawaan yang digunakan untuk mengoperasikan variable bertipe string
    # upper() => ubah setiap huruf menjadi huruf kapital
    # lower() => ubah setiap huruf menjadi huruf kecil
    # split() => Pisahkan teks berdasarkan delimiter (karakter pemisah).
    # title() => Jadikan setiap awal kata kapital.
    # zfill() => Tambahkan nol di awal string sebanyak nilai yang ada pada parameter.

#  regex = regular expression
    # => sebuah cara untuk mencari teks berdasarkan pola tertentu.
import re     # Import modul regex

pola= '^a...s$'
string_tes= 'abyss'
hasil= re.match(pola, string_tes)

if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.") 