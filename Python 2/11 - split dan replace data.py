## split pada python
# split menggunakan slash
data_siswa = "aria/malik/zaki/fadly"
split_data_siswa = data_siswa.split("/")

print(split_data_siswa)

# split menggunakan teks kosong
data_siswa = "aria malik zaki fadly"
split_data_siswa = data_siswa.split()

print(split_data_siswa,"\n")

## replace pada python
# replace ! menjadi ?
data = "yes!"
replace_data = data.replace("!","?")

print(data)
print(replace_data,"\n")

# replace date time
today = "7 agustus 2021"
today = today.replace("7 agustus 2021", "8 agustus 2021")

print(today)