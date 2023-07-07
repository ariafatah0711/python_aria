########################################
print("\n---------pengenalan string---------\n")
########################################

data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup\t\t\totong, semakin jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp 
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD   
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD\new normal 
Website : www.ucup.com/newID
""")

########################################
print("\n----------operasi memanipulasi string----------\n")
########################################

# Operasi dan Memanipulasi String

# 1. Menyambung String (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang " + nama_lengkap + " adalah " + str(panjang))

# 3. operator untuk string

# cek apakah ada komponen pada sebuah string
d = "d"
status = d in nama_lengkap
print("apakah " + d + " ada di " + nama_lengkap + ", " + str(status))

D = "D"
status = D in nama_lengkap
print("apakah " + D + " ada di " + nama_lengkap + ", " + str(status))

x = "x"
status = x not in nama_lengkap
print("apakah " + x + " tidak ada di " + nama_lengkap + ", " + str(status))

# mengulang string
print("wk"*100)
print(100*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0]) # dimulai dari 0
print("index ke-6 : " + nama_lengkap[6]) # index bebas
print("index ke-(-1) : " + nama_lengkap[-1]) # indexing dari dibelakang
print("index ke-[6,8) : " + nama_lengkap[6:8]) # dimulai dari index 6 sampai sebelum 8
print("index ke-[0,2,4,6,8] : " + nama_lengkap[0:10:2]) # diambil index 0,2,4,6,8

# item paling kecil
print("nilai terkecil : " + min(nama_lengkap))
# item paling besar
print("nilai terbesar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII number dari spasi : " + str(ascii_code))
data = 117
print("Character dari ascii code 117 : " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o di " + data + " : " + str(jumlah))


########################################
print("\n---------operasi memanipulasi string 2---------\n")
########################################


# operator dalam bentuk methods

## merubah case pada string

# merubah semua ke upper case
salam = "bro!"
print("normal " + salam)
salam = salam.upper()
print("upper " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieeZZZ"
print("normal " + alay)
alay = alay.lower()
print("lower " + alay)

## method is, untuk pengecekan

# contoh isupper()
salam = "SIST"
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))
salam = salam.lower()
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))

# islower() <- untuk pengecekan apakah lower case semua
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case

judul = "It Is Okay To Not Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))

# startwith() dan endwith() <-- keren

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start " + str(cek_start))
cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end " + str(cek_end))

# join() dan split() <-- buat orang males

pisah = ['aku','sayang','kamu']
gabungan = ' ehm '.join(pisah)
print(pisah)
print(gabungan)

gabungan = "naik vespa keliling kota"
pisah = gabungan.split()
print(gabungan)
print(pisah)

gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm")
print(gabungan)
print(pisah)

# alokasi karakter
print("'kiri      '")

kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
print("'" + kanan + "'")

kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
print("'" + kiri + "'")

tengah ="tengah".center(20) # rata tengah dengan 20 karakter
print("'" + tengah + "'")

tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter
print("'" + tengah + "'")

# kebalikan dari alokasi karakter
kanan = kanan.strip()
print("'" + kanan + "'")
tengah = tengah.strip('-')
print("'" + tengah + "'")