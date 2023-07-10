''' default argument '''

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

# contoh tanpa default
def say_hello1(nama1):
    '''fungsi dengan default argument'''
    print(f"halo {nama1}")

# pake argument      
say_hello1("aria fatah")

# pake default
def say_hello2(nama2 = "kamu"):
    '''fungsi dengan default argument'''
    print(f"halo {nama2}\n")

# tanpa argument
say_hello2()

# 2 argument
def sapa_dia(nama, pesan = "apa kabar?"):
    '''fungsi dengan input biasa dan satu default argument'''
    print(f"hai {nama}, {pesan}")

sapa_dia("dudung", "kamu ganteng")
sapa_dia("dudung")

# contoh 3
def hitung_pangkat(angka = 0, pangkat = 1):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(2,4))

# memilih parameter
hasil = hitung_pangkat(pangkat=2, angka=5)
print(hasil)

# default
default = hitung_pangkat()
print(default)

# contoh 4
def fungsi(input1 = 1, input2 = 2, input3 = 3, input4 = 4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print("\ndefault", fungsi())
print("with input", fungsi(input2 = 1, input3 = 1, input4= 1))