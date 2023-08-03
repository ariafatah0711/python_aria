import time, datetime, os
# data
harga = 0
saldo = 0

# List Top Up diamond
def list():
	print("\033[36;1m    LIST TOP UP DIAMOND MOBILE LEGEND\033[37;1m")
	print("\033[33;1m----------------------------------------")
	print("|NO| JUMLAH DIAMOND \t|  HARGA       |")
	print("----------------------------------------")
	print("|1.| 12 Diamonds \t| Rp. 3.500    |")
	print("|2.| 56 Diamonds \t| Rp. 16.000   |")
	print("|3.| 169 Diamonds \t| Rp. 49.000   |")
	print("|4.| 366 Diamonds \t| Rp. 100.000  |")
	print("|5.| 568 Diamonds \t| Rp. 230.000  |")
	print("|6.| 1455 Diamonds \t| Rp. 390.000  |")
	print("|7.| 2010 Diamonds \t| Rp. 525.000  |")
	print("|8.| 3638 Diamonds \t| Rp. 980.000  |")
	print("----------------------------------------")

# input jumlah diamond
while True:
	os.system("clear")
	list()	
	x = input("\033[37;1mmasukan kode diamond yang ingin dibeli: ")
	if x == "1":
		item = "12 Diamond"
		harga += 3500
		break
	elif x == "2":
		item = "56 Diamond"
		harga += 16000
		break
	elif x == "3":
		item = "169 Diamond"
		harga += 49000
		break
	elif x == "4":
		item = "366 Diamond"
		harga += 100000
		break
	elif x == "5":
		item = "568 Diamond"
		harga += 230000
		break
	elif x == "6":
		item = "1455 Diamond"
		harga += 390000
		break
	elif x == "7":
		item = "2010 Diamond"
		harga += 525000
		break
	elif x == "8":
		item = "3638 Diamond"
		harga += 980000
		break
	else:
		print("\033[31;1mjumlah diamond tidak ada di dalam daftar\033[37;1m")
		time.sleep(1)
		os.system("clear")
		continue

time.sleep(1)
print("\033[36;1m\npesanan diamond mobile legend\033[37;1m")
print("----------------------------------------")
print("jumlah diamond \t\t:", item)
print("harga pembayaran \t: Rp.", harga)
time.sleep(1)

# input ID ml
# input id hanya bisa di input jika teks lebih dari 5 dan kurang dari 8
def syarat_id(id_ml):
  if len(id_ml) < 5 or len(id_ml) > 8:
    return False
  return True

while True:
	id_ml = input("\nMasukkan ID game\t: ")
	time.sleep(0.5)
	if syarat_id(id_ml):
		print("\033[32;1mID mobile legend valid\n\033[37;1m")
		print("\033[36;1msilakan lanjutkan ke meteode pembayaran.\033[37;1m")
		print("----------------------------------------")
		time.sleep(1)
		break
	else:
		print("\033[31;1mID mobile legend tidak valid\033[37;1m")			

# input no telp
# input no telp hanya bisa di input jika teks input lebih dari 10 dan kurang dari 14
# dan no telp harus diawali nomer 08			
def syarat_telp(telp):
  if len(telp) < 10 or len(telp) > 14:
    return False
  if not telp.startswith("08"):
    return False
  return True

while True:
	telp = input("Masukkan nomor telepon \t: ")
	time.sleep(0.5)
	if syarat_telp(telp):
		print("\033[32;1mNomor telepon valid\033[37;1m")
		time.sleep(1)
		break
	else:
		print("\033[31;1mNomor telepon tidak valid\n\033[37;1m")

# input saldo pembayaran
while True:
	try:
		saldo_anda = int(input("\nmasukan uang pembayaran: "))
	except ValueError:
			time.sleep(0.5)
			print("\033[31;1mpembayaran harus angka silakan coba lagi!\033[37;1m")
			continue	
	time.sleep(1)
	saldo += saldo_anda		
	if saldo == harga:
		print("\033[36;1muang anda pas!\033[37;1m")
		break
	elif saldo >= harga:
		print("\033[36;1mkembalianya\033[37;1m", saldo - harga)
		break
	else:
		print("\033[31;1muang anda kurang!\033[37;1m", saldo - harga)
		time.sleep(0.5)

# struck pembayaran
time.sleep(0.2)
print("\033[32;1m\npembelian berhasil!\033[37;1m")
print("diamond telah ditambahkan ke dalam game anda.\n")
time.sleep(1)
print("\033[36;1mBukti pembayaran\033[37;1m")
print("\033[33;1m-----------------------------------------")
print("ID mobile legend \t:", id_ml, "\t|")
print("jumlah diamond \t\t:", item, "\t|")
print("no telp pembayaran \t:", telp, "\t|")
print("harga pembayaran \t: Rp.", harga, "\t|")
print("saldo pembayaran \t: Rp.", saldo, "\t|")
print("kembalianya \t\t: Rp.", saldo - harga, "\t|")

# waktu
jam = datetime.datetime.now().time()
time = jam.strftime("%I:%M %p")
print("waktu pembelian \t:", time, "\t|")
print("-----------------------------------------\033[37;1m")