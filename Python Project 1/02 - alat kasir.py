import os, time
# data
barang = [ ]
harga = [ ]
total = 0
pesanan = 0
saldo = 0

# list menu
while True:
	os.system("clear")
	print("\t\033[36;1mLIST MENU CHICKEN\033[37;1m")
	print("\033[33;1m------------------------------------")
	print("|NO| PESANAN \t\t|  HARGA   |")
	print("------------------------------------")
	print("|1.| kentang \t\t| Rp. 6000 |")
	print("|2.| sayap \t\t| Rp. 7000 |")
	print("|3.| paha bawah \t| Rp. 8000 |")
	print("|4.| paha atas \t\t| Rp. 10000|")
	print("|5.| dada \t\t| Rp. 11000|")
	print("------------------------------------")
	print("|#.| \033[36;1mtotal pesanan \t\033[33;1m| \033[32;1m", pesanan, "\t   \033[33;1m|")
	print("------------------------------------")
	print("\n\033[36;1mX untuk exit | Y untuk berhenti\033[37;1m")
	
# pilih pesanan
	x = input("masukan kode barang: ")
	if x == "1":
		barang.append("kentang")
		harga.append(6000)
		total += 6000
		pesanan += 1
		os.system("clear")
	elif x == "2":
		barang.append("sayap ayam")
		harga.append(7000)
		total += 7000
		pesanan += 1
		os.system("clear")
	elif x == "3":
		barang.append("paha bawah")
		harga.append(8000)
		total += 8000
		pesanan += 1
		os.system("clear")
	elif x == "4":
		barang.append("paha atas")
		harga.append(10000)
		total += 10000
		pesanan += 1
		os.system("clear")
	elif x == "5":
		barang.append("dada ayam")
		harga.append(11000)
		total += 11000
		pesanan += 1
		os.system("clear")
	elif x == "y":
		break
	elif x == "x":
		print("\nprogam berhenti")
		exit()
	else:
		print("kode anda salah!!!")
		time.sleep(1)
		os.system("clear")
		
# data pesanan
time.sleep(1)
print("\n\033[32;1mdaftar pesanan \t\033[37;1m: ", ', ' .join(barang))
print("\033[32;1mharga pesanan \t\033[37;1m: ", ", ".join(map(str, harga)))
print("\033[32;1mtotal pesanan \t\033[37;1m:  Rp.", total)
time.sleep(1)

# pembayaran
while True:
	try:
		saldo_anda = int(input("\n\033[37;1mmasukan uang pembayaran:\033[36;1m "))
		time.sleep(1)
	except ValueError:
		print("\033[31;1mpembayaran harus angka. silakan coba lagi!")
		continue
		
	saldo += saldo_anda
	if saldo == total:
		print("\033[32;1muang anda pas\033[37;1m")
		break
	elif saldo >= total:
		print("\033[32;1mkembalianya \033[36;1m\t:  Rp.", saldo - total, "\033[37;1m")
		break
	else:
		print("\033[31;1muangnya kurang\t\033[36;1m : ", saldo - total, "\033[37;1m")