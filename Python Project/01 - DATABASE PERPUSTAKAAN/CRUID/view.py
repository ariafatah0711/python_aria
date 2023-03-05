from . import operasi
import os, time, sys

def lanjut():
    global x
    is_done = input("Apakah Selesai (y/n)? ")

    if is_done == "y" or is_done == "Y":
        x = True

    else:
        x = False

# Read_Data
def read_console():
    os.system("clear")
    data_file = operasi.read()

    index = "No"
    judul = "judul"
    penulis = "penulis"
    tahun = "tahuun"

    # header
    print("="*102)
    print(f'|{"DATA BASE PERPUSTAKAAN":^100}|')
    print(f'|{"Read Data":^100}|')
    print("="*102)
    print(f"|{index:^4} | {judul:40} | {penulis:40} | {tahun:5} |")
    print("-"*102)

    global v
    v = True

    # data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]

        print(f"|{index+1:^4} | {judul:.40} | {penulis:.40} | {tahun.strip():7}", end="|\n")

    # footer
    print("="*102, "\n")

# Create_Data
def create_console():
    while True:
        try:
            os.system("clear")
            print("="*32)
            print(f'|{"DATA BASE PERPUSTAKAAN":^30}|')
            print(f'|{"CREATE FILE":^30}|')
            print("="*32)

            penulis = input("| penulis : ")
            judul = input("| judul\t  : ")
            tahun = int(input("| tahun\t  : "))

            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus terdiri 4 angka, silakan masukan lagi (yyyy)")
                time.sleep(1)
        except:
            print("tahun harus angka, silakan masukan lagi (yyyy)")
            time.sleep(1)

    operasi.create(tahun, judul, penulis)
    global v
    if operasi.x == True:
        print("\nberikut adalah data baru anda")
        time.sleep(1.5)
        read_console()
        v = True
    elif operasi.x == False:
        v = False
        
def update_console():
    global v,x
    x = True
    v = True
    while True:
        print("silakan pilih no buku")
        read_console()
        no_buku = int(input("no buku: "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("nomor tidak valid silakan coba lagi")

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1]

    print(pk)
    print(data_add)
    print(judul)
    print(penulis)
    print(tahun)

    print(data_buku)