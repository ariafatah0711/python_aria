# class
# istensi

class mahasiswa():
    nama = "nama" # ini namanya atribut
    kelas = "tidak ada"

    #__init__ itu akan terpanggil jika kita memangil mahasiswa()
    def __init__(self, input_nama, input_kelas): # ini seperti kondisi utama jika class dipanggil
        # print("ini adalah init")
        self.nama = input_nama
        self.kelas = input_kelas

    def belajar(self, kondisi): # ini namanya method
        print(self.nama, self.kelas, "sedang belajar", kondisi, "\n")

    def tidur(self, kondisi):
        print(f"{self.nama} {self.kelas} sedang tidur {kondisi}")


## 1. otong
# pengenalan
otong = mahasiswa("otong surotong", "x.tkj.1")

# artinya otong.nama = mahasiswa.nama = ""
'''otong.nama = "otong surotong"'''

# method
otong.belajar("dengan giat")

# kesimpulanya adalah otong.belajar adalah mahasiswa.belajar()
# dialam belajar terdapat self fugsi seperti variable yg memanggilnya
# otong.nama itu sama dengan otong.self

## 2. ucup
# ucup = mahasiswa()
# ucup.nama = "ucup ganz"
# ucup.tidur("di kelas")

## 2. aria
aria = mahasiswa("aria fatah anom", "x.tkj.1")
aria.belajar("bahasa inggris")
print(aria.nama)
print(aria.kelas, "\n")

# atribut dapat diubah
aria.nama = "aria ganteng"
print(aria.nama)