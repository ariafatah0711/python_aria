# class variable
class mahasiswa():

    jurusan = "ekonomi"
    
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # atribut publik
        self.nim = input_nim 

# main progam

aria = mahasiswa("aria fatah", "x.tkj.1")
malik = mahasiswa("muhamad malik", "x.tkj.1")

mahasiswa.jurusan = "ekonomi it"
malik.jurusan = "it doang"

# __dict__
print(aria.jurusan)
print(malik.jurusan)
print(mahasiswa.jurusan, "\n")

print(mahasiswa.__dict__["jurusan"])
print(malik.__dict__)

# variable
aria.jurusan = "tkj"
aria.kegemaran = "menonton anime"
print(aria.kegemaran)

print("\n", aria.__dict__)

class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # atribut publik
        self.nim = input_nim 

        mahasiswa.jumlah_mahasiswa += 1

aria = mahasiswa("aria", 29834)
malik = mahasiswa("malik", 29834)
zaki = mahasiswa("zaki", 29834)

# yang terjiadi adalah ketika ada mahasiswa yang di panggil maka akan menjalankan init
print(mahasiswa.jumlah_mahasiswa)