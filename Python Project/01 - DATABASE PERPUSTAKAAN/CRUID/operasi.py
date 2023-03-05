import time, os
from . import Database
from .util import random_string

def head():
    os.system("clear")
    print("="*32)
    print(f'|{"DATA BASE PERPUSTAKAAN":^30}|')
    print(f'|{"NEW FILE":^30}|')
    print("="*32)

def create_first_data():
    while True:
        try:
            head()
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

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    # data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%z", time.gmtime())
    data["date_add"] = time.strftime("%d-%m-%y", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    print(f'| Keys\t  : {data["pk"]}')
    print(f'| date\t  : {data["date_add"]}')
    print("="*32)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}'

    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("File tidak dapat ditambahkan!")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            global x
            x = True

            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("membaca Database error")
        return False

def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    # data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%z", time.gmtime())
    data["date_add"] = time.strftime("%d-%m-%y", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    print(f'| Keys\t  : {data["pk"]}')
    print(f'| date\t  : {data["date_add"]}')
    print("="*32)

    is_lanjut = input("tambahkan Data? ")
    global x
    if is_lanjut == "y" or is_lanjut == "Y":
        data_str = f'\n{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}, '
        try:
            with open(Database.DB_NAME, "a", encoding="utf-8") as file:
                file.write(data_str)
                x = True
        except:
            print("\nFile tidak dapat ditambahkan!")
    else:
        print("\ndata tidak di Create")
        time.sleep(1)
        x = False
        