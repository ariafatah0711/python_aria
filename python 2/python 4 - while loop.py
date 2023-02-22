
# while loop

# while kondisi:
# 	aksi ini
# 	aksi itu

# akhir dari program

angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
	angka += 1
	print(f"angka sekarang -> {angka}")
	print("otong ganteng maxsyimaal!")

print("cukuuup")

###################

# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

# angka = 0

# while angka < 5:
# 	angka += 1

# 	if angka == 3:
# 		pass # ini tidak akan dieksekusi

# 	print(angka)

# continue

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
	angka += 1
	print(f"angka sekarang -> {angka}") # aksi 1

	if angka == 3:
		print("nice!")
		continue # akan membuat loop meloncat ke step selanjutnya

	print("whassup!") # aksi 2

print("Pinish!")

##################


# Break
angka = 0

while angka < 5:
	angka += 1
	print(f"angka sekarang = {angka}")

	if angka == 3:
		print("nice!")
		break

	print("wassup!")

print("cukuuup finish!")

data_int = int(input("hitung sampai = "))

angka = 0

while True:
	angka += 1
	print(f"count = {angka}")

	if angka == data_int:
		print("nice!")
		break

	print("wassup!")

print("cukuuup finish!")

#######################

# Latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan For

# dummy variable
print("awal For")
count = 1
for i in range(sisi):
	print("*"*count)
	count += 1

print("akhir dari for")
# 2. Menggunakan while

print("awal while")
count = 1
while True:
	print("*"*count)
	count += 1

	if count > sisi:
		break

print("akhier while")

# 3. hanya ganjil saja

print("awal while")
count = 1
while True:
	if (count%2):
		# Print jika ganjil
		print("*"*count)
		count += 1
	else:
		# akan kembali ke atas jika ganjil
		count += 1
		continue

	# akan break jika count melebihi sisi
	if count > sisi:
		break

print("akhier while")

# 4. hanya ganjil saja

print("awal while")
count = 1
spasi = int(sisi/2)

while True:
	if (count%2):
		# Print jika ganjil
		print(" "*spasi,"+"*count)
		spasi -= 1
		count += 1
	else:
		# akan kembali ke atas jika ganjil
		count += 1
		continue

	# akan break jika count melebihi sisi
	if count > sisi:
		break

print("akhier while")