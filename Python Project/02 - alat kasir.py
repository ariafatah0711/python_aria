import os, time
# data
barang = [ ]
harga = [ ]
total = 0
pesanan = 0
saldo = 0

# list menu
while True:
	print("\tLIST MENU CHICKEN")
	print("------------------------------------")
	print("|NO| PESANAN \t\t|  HARGA   |")
	print("------------------------------------")
	print("|1.| kentang \t\t| Rp. 6000 |")
	print("|2.| sayap \t\t| Rp. 7000 |")
	print("|3.| paha bawah \t| Rp. 8000 |")
	print("|4.| paha atas \t\t| Rp. 10000|")
	print("|5.| dada \t\t| Rp. 11000|")
	print("------------------------------------")
	print("|#.| total pesanan \t| ", pesanan, "\t   |")
	print("------------------------------------")
	print("\nX untuk exit | Y untuk berhenti")
	
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
		exit()
	else:
		print("kode anda salah!!!")
		time.sleep(1)
		os.system("clear")
		
# data pesanan
time.sleep(1)
print("\ndaftar pesanan \t: ", ', ' .join(barang))
print("harga pesanan \t: ", ", ".join(map(str, harga)))
print("total pesanan \t:  Rp.", total)
time.sleep(1)

# pembayaran
while True:
	try:
		saldo_anda = int(input("\nmasukan uang pembayaran: "))
		time.sleep(1)
	except ValueError:
		print("pembayaran harus angka. silakan coba lagi!")
		continue
		
	saldo += saldo_anda
	if saldo == total:
		print("uang anda pas")
		break
	elif saldo >= total:
		print("kembalianya \t:  Rp.", saldo - total)
		break
	else:
		print("uangnya kurang\t : ", saldo - total)