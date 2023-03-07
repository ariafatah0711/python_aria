''' fungsi dengan kembalian'''
''' return value '''

# tanpa return
import cmd


def fungsi_tanpa_return(parameter):
    hasil = parameter**2

z = fungsi_tanpa_return(10)
print(z) # outputnya: none karena nilai hasil tidak dimasukan ke dalam variable z
# z = none

# pake return
def fungsi(parameter):
    hasil = parameter**2
    return hasil # artinya nilai hasil di masukan ke dalam variable 

y = fungsi(10)
print(y)
# y = hasil / 10**2 = 100

'''#######################'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#     badan fungsi
#     return output

def luas(x):
    output = x * 4
    return output

c = luas(10)
print(c)
# bisa juga langsung di print
print(luas(100))

# bisa juga ditambahkan
total = c + luas(100)
print(total)

# def tambah
def fungsi_tambah(angka_1,angka_2):
    '''fungsi return dengan multi parameter'''
    return angka_1 + angka_2

a = fungsi_tambah(10,5)
print(a, "\n")

# fungsi dengan return banyak
def operasi_aritmatika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    # return sekalisgus/multi
    return tambah,kurang,kali,bagi
# urutan return mempengaruhi output variable

# format k,l,m,n artinya membuat 4 variable dan membagi 4 value
k,l,m,n = operasi_aritmatika(10,2)

print(f"10 dan 2")
print(f"hasil tambah = {k}")
print(f"hasil kurang = {l}")
print(f"hasil kali = {m}")
print(f"hasil bagi = {n}")