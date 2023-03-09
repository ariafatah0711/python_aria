from . import operasi
import os, time

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
    tahun = "tahun"

    # header
    print("="*102)
    print(f'|{"DATA BASE PERPUSTAKAAN":^100}|')
    print(f'|{"Read Data":^100}|')
    print("="*102)
    print(f"|{index:^4} | {judul:40} | {penulis:40} | {tahun:6} |")
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

        print(f"|{index+1:^4} | {judul:<.40} | {penulis:<.40} | {tahun.strip():7}", end="|\n")

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

    operasi.create(tahun,judul,penulis)
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
    x = False
    v = False
    while True:
        read_console()
        print("silakan pilih no buku yang ingin di update")
        try:
            no_buku = int(input("no buku: "))
        except:
            continue
        
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("nomor tidak valid, silakan coba lagi")

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while True:
        os.system("clear")
        print(""+"="*102)
        print(f'|{"DATA BASE PERPUSTAKAAN":^100}|')
        print(f'|{f"UPDATE BUKU KE -{no_buku}":^100}|')
        print("="*102)

        print(f'| 1. Judul \t: {judul:.<.70} \t     |')
        print(f'| 2. Penulis \t: {penulis:.<.70} \t     |')
        print(f'| 3. Tahun \t: {tahun:<70} \t     |')
        print("="*102)

        user_option = input("| pilih data [1,2,3]: ")
        print("="*102)

        match user_option:
            case "1": judul = input("| 1. judul \t: ")
            case "2": penulis = input("| 2. penulis \t: ")
            case "3": 
                while True:
                    try:
                        tahun = int(input("| 3. tahun \t:  "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("tahun harus terdiri 4 angka, silakan masukan lagi (yyyy)")
                            time.sleep(1)
                    except:
                        print("tahun harus angka, silakan masukan lagi (yyyy)")
                        time.sleep(1)
            case "y":
                break
            case _:
                print("index tidak cocok")
                continue

    operasi.update(no_buku,pk,data_add,tahun,judul,penulis)

    x = False
    v = False

def delete_console():
    global v, x
    v, x = True, True
    read_console()

    while True:
        read_console()
        print("silakan pilih no buku yang ingin di Delete")
        try:
            no_buku = int(input("no buku: "))
        except:
            continue

        data_buku = operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = str(data_break[4][:-1])
            
            os.system("clear")
            print(""+"="*102)
            print(f'|{"DATA BASE PERPUSTAKAAN":^100}|')
            print(f'|{f"DELETE BUKU KE -{no_buku}":^100}|')
            print("="*102)

            print(f'| 1. Judul \t: {judul:.70} \t     |')
            print(f'| 2. Penulis \t: {penulis:.70} \t     |')
            print(f'| 3. Tahun \t: {tahun:<70} \t     |')
            print("="*102)

            is_done = input("Menghapus Data (y/n)? ")
            if is_done == "y" or is_done == "Y":
                x, v = False, False
                operasi.delete(no_buku)
                time.sleep(1)
                break
                
            elif is_done == "n" or is_done == "N":
                x, v = False, False
                break
            else:
                x, v = False, False
                continue
        else:
            print("nomor tidak valid, silakan coba lagi")
