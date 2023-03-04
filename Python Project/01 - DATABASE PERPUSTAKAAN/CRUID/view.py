from . import operasi
import os

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