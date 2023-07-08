#contoh menggunakan fungsi
save = [1, 2, 3]

def tambah(angka):
    return angka + 10

hasil = [tambah(item) for item in save]
print(hasil)

# contoh menggunakan if
password = ["12345678", "abcdefgh", "!@#$%^&*()"]

# cuma ngeteas ga ush diikuti
# for i in password:
#     if len(str(i)) > 8:print(value)

valid = [valided for valided in password if valided.count("@") > 0]
print(valid) # kesimpulanya variable valided di loop dan ditambahkan kondisi jika valided memiliki @ akan ditampilkan

# menambahkan https pada semua list
websites = ["facebook.com", "mimo.com", "food.org"]

def add_https(site):
    return "https://" + site

auto_add = [add_https(site) for site in websites]
print(auto_add)