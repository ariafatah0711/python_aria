## Exeception akan terjadi saat
# ada error / kesalahan saat runtime
from math import nan

# 1. ZeroDivisionError: division by zero
'''
# terjadi ketika kita menginput data dan mengisi angka 0
# 10/0 itu tidak akan dapat berjalan'''
data_input = int(input("masukan angka: "))
hasil = 10/data_input
print(hasil)

# 2. SyntaxError:
'''
# syntak error adalah kesalahan pada penulisan
# SyntaxError: '(' was never closed
# artinya ( ini blum tertutup'''
# print(hasil

# 3. FileNotFoundError:
'''
# FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
# artinya file tidak ditemukan tidak adanya file data.txt'''
# file = open("data.txt", "r")


# 4. NameError: name 'nan' is not defined
'''
# ini adalah error yang dikarenakan saat kita membuat variable dan di dalamnya ada kata namun tidak terdefinisi
# atau tidak ada maka akan menmpilkan kesalahan
'''
# waktu = datetiime.datetime.now()

# 5. ModuleNotFoundError: No module named 'ueifnei'
'''
# terjadi ketika kita mengimport module namun kita tidak memilikinya
'''
# import ueifnei

# 6. ValueError: invalid literal for int() with base 10: 'a'
'''
# artinya value/data error karena kita menginput yang bukan seharusnya
# terjadi ketika kita menginput int namun kita mengetikan string'''
# int = int(input("masukan angka")) = jika kita menulis string progam akan value error

# 7. TypeError: exceptions must derive from BaseException
'''
# mirip dengan value error
# type dari variablenya salah dan tidak sesuai
# type int tidak bisa dioperand dengan type string'''
# a,b = 5,"v"
# hasil = a+b

## contoh untuk mengatasiya
# contoh 1:
input_user = int(input("masukan angka: "))
hasil = nan

try:
    hasil = 10/input_user
except:
    print("hasil atau input tidak boleh 0")

# artinya setelah kita menginput kita progam akan Try hasil/10
# jika error maka progam akan except dan print("hasil input tidak boelh 0")
print(f"hasil: {hasil}")

# contoh 2
while(True):
    angka = int(input("masukan angka pembagi: "))
    try:
        hasil = 10/angka
        print(f"hasil dari 10/{angka}: {hasil}")
        is_done = input("lanjutkan (Y/N)? ")
        if is_done == "n":
            break
        else:
            continue
    except:
        print("pembagi nol, silakan masukan angka lagi")
    # artinya jika try ada kesalahan dia akan otomatis lanjut ke except dan menskip try

print("akhir dari progam 1")

# contoh 3
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("file baru")

print("akhir dari progam 2")