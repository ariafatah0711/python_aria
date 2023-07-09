import datetime

mahasiswa1 = {
    "nama":"aria fatah",
    "nim":"291038439",
    "sks_lulus":140,
    "beasiswa":True,
    "lahir":datetime.datetime(2006,11,7)
}

mahasiswa2 = {
    "nama":"vido",
    "nim":"291038343",
    "sks_lulus":120,
    "beasiswa":False,
    "lahir":datetime.datetime(2007,8,13)
}

mahasiswa3 = {
    "nama":"fadly",
    "nim":"2910355649",
    "sks_lulus":130,
    "beasiswa":False,
    "lahir":datetime.datetime(2006,12,24)
}

data_mahasiswa = {
    "mah001":mahasiswa1,
    "mah002":mahasiswa2,
    "mah003":mahasiswa3
}

# pemformatan {"string:<100"} <100 panjang teks string
# <10 artinya teks ada di kiri sampai 10
# ^10 artinya teks center/tengah
# >10 artinya teks ada di kanan
print(f"{'key':<6} {'nama':<17} {'sks':<3} {'beasiswa':<9} {'lahir':<10}")
print("-"*50)

# biar bagus pake for
for mahasiswa in data_mahasiswa:
    key = mahasiswa

    nama = data_mahasiswa[key]["nama"]
    nim = data_mahasiswa[key]["nim"]
    sks = data_mahasiswa[key]["sks_lulus"]
    beasiswa = data_mahasiswa[key]["beasiswa"]
    lahir = data_mahasiswa[key]["lahir"].strftime("%x")

    print(f"{key:<6} {nama:<17} {sks:<3} {beasiswa:^9} {lahir:<10}")