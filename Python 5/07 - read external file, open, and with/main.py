## tutorial membaca  file external
print(3*"=", "membaca file.txt", 3*"=")

file = open("data.txt", mode="r") # modenya untul read, 

print(f"status read: {file.readable()}") # mengecek apakah dia bisa di read
print(f"status read: {file.writable()}") # mengecek apakah dia bisa di write

## baca seluruh file
'''
print(file.read()) ''' # artinya variable file yang isinya data.txt di read/baca

## baca baris per baris
# print(file.readline(),end="") # membaca baris pertama # end artinya akhirnya kosong dan tidak di spasi
# print(file.readline()) # membaca baris ke-2

## baca semua baris sebagai list
print(file.readlines())

print(f"apakah file sudah di close: {file.closed}") # apakah file sudah ditutup
file.close # untuk close
print(f"apakah file sudah di close: {file.closed}") # apakah file sudah ditutup

## salah satu teknik membuka file di python
print("\n", 3*"=", "membaca file.txt", 3*"=")

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah di close: {file.closed}") # apakah file sudah ditutup

print(f"apakah file sudah di close: {file.closed}") # apakah file sudah ditutup