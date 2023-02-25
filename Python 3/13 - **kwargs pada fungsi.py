''' **kwargs '''

# fungsi biasa
def fungsi_biasa(nama,tinggi,berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_biasa("aria",180,80)

# pake **kwargs
def fungsi_kwargs(**kwargs):
    '''fungsi kawrgs'''
    print(kwargs) # hasilnya dictionary
    
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_kwargs(nama="aria",tinggi=180,berat=80)
# kwagrs bisa bikin dictionary

# studi kasus
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        print("operasi penjumlahan")
        for angka in args:
            output += angka

    elif kwargs["option"] == "kali":
        print("operasi perkalian")
        output = 1 # kenapa output 1 karena saat kita menggunakan 0 perkalianya akan sprti 0 * 1 dan hasilnya akan ttp 0
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")
    return output

hasil1 = math(1,2,3,4,option="tambah")
hasil2 = math(1,2,3,option="kali")

print(f"hasil tambah: {hasil1}")
print(f"hasil kali: {hasil2}")