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
    head()
    penulis = input("| penulis : ")
    judul = input("| judul\t  : ")
    tahun = input("| tahun\t  : ")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    # data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%z", time.gmtime())
    data["date_add"] = time.strftime("%d-%m-%y", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    print(f'| Keys\t  : {data["pk"]}')
    print(f'| date\t  : {data["date_add"]}')
    print("="*32)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}'

    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("ada kesalahan dalam file")

def read():
    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            return content
    except:
        print("membaca Database error")
        return False