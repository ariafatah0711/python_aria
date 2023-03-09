from . import operasi
import time

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"xxxxxx",
    "date_add":"YYYY-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("checking Database, wait...")
            time.sleep(1.4)
            print("Database tersedia, init done!")
            time.sleep(0.7)

    except:
        print("checking Database, wait...")
        time.sleep(1.4)
        print("Database tidak ditemukan")
        time.sleep(1)
        print("silakan membuat data base baru!")
        time.sleep(0.7)
        operasi.create_first_data()