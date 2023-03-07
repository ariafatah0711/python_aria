class mahasiswa():
    jurusan = "tkj"
    __nilai = 0 # atribut privat tidak dapat diakses

    #__init__ itu akan terpanggil jika kita memangil mahasiswa()
    def __init__(self, input_nama, input_kelas): # ini seperti kondisi utama jika class dipanggil
        # print("ini adalah init")
        self.nama = input_nama # publik
        self.kelas = input_kelas 
        self.__nilai = 0 # ini default

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama, "tidak lulus")
        else:
            print(self.nama, "lulus")

# main progam
aria = mahasiswa("aria fatah", "x.tkj.1")
malik = mahasiswa("muhammad abdul malik", "3A")

# print(aria.__nilai)
# # print(aria.nilai)

aria.uts(70)
aria.uas(85)

aria.check_status()

malik.uts(10)
malik.uas(25)

malik.check_status()