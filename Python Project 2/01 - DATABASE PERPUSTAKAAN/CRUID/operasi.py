from time import time
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

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

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

def create(tahun,judul,penulis):
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
        data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
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

def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    # if no_buku == 0:  
    #     data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    # else:
    #     data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku - 1))
            file.write(data_str)
    except:
        print("\nFile tidak dapat diubah!")

def delete(no_buku):
    try:
        with (open(Database.DB_NAME, "r")) as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1 :
                    pass
                else:
                    with open("data_temp.txt", "a", encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1

    except:
        print("Database Error")

    try:
        os.rename("data_temp.txt",Database.DB_NAME)
        print("data berhasil di hapus")
    except:
        print("Data minimal memiliki 1 buku")
        time.sleep(2)