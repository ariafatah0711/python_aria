'''latihan fungsi'''
import os

'''
# progam menghitung luas dan persegi panjang
# header
os.system("clear")
print(f"{'PROGAM MENGHITUNG LUAS':^40}")
print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
print(f"{'-'*40:^40}")

# mengambil input user
lebar = int(input("masukan nilai lebar: "))
panjang = int(input("masukan nilai panjang: "))

# progam menghitung luas
luas = panjang * lebar
keliling = 2 * (panjang+lebar)

# tampilan hasilnya
print(f"hasil perhitungan luas = {luas}")
print(f"hasil perhitungan keliling = {keliling}")'''

def header():
    os.system("clear")
    print(f"{'PROGAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # mengambil input user
    lebar = int(input("masukan nilai lebar: "))
    panjang = int(input("masukan nilai panjang: "))
    # menaruh lebar dan panjang ke L dan B
    return lebar, panjang

def hitung_luas(lebar, panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar, panjang):
    '''fungsi keliling'''
    return 2 * (lebar*panjang)

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")


# progam utama
while True:
    header()
     # data
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    # PR
    opsi = input("pilih 1 untuk luas, 2 untuk kelilling 3 dua duanya: ")
    if opsi == "1":
        display("luas", LUAS)

    elif opsi == "2":
        display("keliling", KELILING)

    elif opsi == "3":
        display("luas", LUAS)
        display("keliling", KELILING)

    else:
        continue

    # lajut atau berhenti
    isContinue = input("apakah lanjut (Y?N)? ")
    if isContinue == "n":
        break

print("progam selesai, terima kasih")

