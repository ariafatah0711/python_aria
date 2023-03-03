# __main__ 
# adalah top level code enveironment

## __name__ == __main__ akan terjadi jika ada di progam file utama
# sebagai progam utama
print(f"nilai __name__ pada main.py: {__name__}") # artinya progam ini dijalankan sebagai progam utama

## __name__ pada file progam external
import fungsi

## contoh penggunaan

# deklarasi
def fungsi_tambah(a:int,b:int)->int:
    return a + b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"hasil tambah: {hasil}")

## import package
import package # artinya adalah ketika kita mengimport package yang berupa folder
# dan didalam folder itu terdapat __main__.py maka dia akan bisa dipanggil
# menggunakan python package dan akan keluar file __main__.py

# ini sama saja dengan python -m venv
# atau python -m package