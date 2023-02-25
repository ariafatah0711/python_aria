'''*args'''

# memasukan data/argumen

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("aria",170,50)

# pake list
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["aria",180,55])

# kenalan dengan *args args artinya argumen

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("aria",180,55)

# studi kasus
def tambah(*data):
    #  data tipenya tupple, dan dia bisa si iterasi
    output = 0
    for angka in data:
        output += angka
        # artinya output 0 ditambah angka yang ada di data namun di ambil satu satu
        # 0 + 1, + 2, ...

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil: {hasil}")

hasil = tambah(1,2,3)
print(f"hasil: {hasil}")