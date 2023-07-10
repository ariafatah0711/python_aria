'''membuat fungsi'''
def hello_world():
    # fungsi menampilkan hello world
    print("helo world")
    print("kepada aria fatah anom")
    print("dan juga kepada otong")

# panggil
hello_world()

'''membuat fungsi'''
def fungsi():
    # pemanggilan fungsi harus ada setelah dibuat
    print("ini fungsi\n")

# panggil
fungsi()

# pengenalan fungsi dengan argumen/input/parameter

def nama_fungsi(parameter):
    # badan fungsi
    '''fungsi hello world menerima input'''
    print(f"selamat datang dunia wahai {parameter}")

nama_fungsi("aria fatah")

# progam pertamabahan
def tambah(angka1, angka2):
    '''fungsi tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1, 10)
tambah(100, 1)

# say hi
def say_hi(peserta):
    '''fungsi say hi'''
    data_peserta = peserta.copy()
    for member in data_peserta:
        print(f"yang terhormat {member}")

anggota = ["aria", "ucup", "otong", "dudung"]

say_hi(anggota)
# anggota adalah parameter peserta