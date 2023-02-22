data_angka = [1,1,2,4,6,2,1,9]

print(f"data angka: {data_angka}\n")

# count data
# menmenghitung jumlah angka 4 dan 3 pada list

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4: {jumlah_data_4}")
print(f"jumlah angka 3: {jumlah_data_3}")

# ambil posisi data 

data = ["ucup", "otong", "dudung", "ujang"]

print(f"data: {data}")

index_dudung = data.index("dudung")
index_ujang = data.index("ujang")

print(f"index dudung: {index_dudung}")
print(f"index ujang: {index_ujang}")

# mengurutkan list
print(f"\ndata angka sebelum di sort: {data_angka}")
data_angka.sort()
print(f"data angka setelah di sort: {data_angka}")

print(f"\ndata sebelum di sort: {data}")
data.sort()
print(f"data setelah di sort: {data}")

# balik list
data_angka.reverse()
data.reverse()
print(f"\ndata angka setelah di revese: {data_angka}")
print(f"data setelah di revese: {data}")