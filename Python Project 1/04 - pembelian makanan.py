import os

while True:
	menu = {
	    "Ice cream":10000,
	    "Cappucino":15000,
	    "Thai Tea":12000,
	    "Matcha Coffee":17000,
	    "Light Coffee":20000,
	    "Donuts Toping":14000,
	    "Burger Hot":18000,
	}
	
	list_menu = {
		"1":menu["Ice cream"],
		"2":menu["Cappucino"],
		"3":menu["Thai Tea"],
		"4":menu["Matcha Coffee"],
		"5":menu["Light Coffee"],
		"6":menu["Donuts Toping"],
		"7":menu["Burger Hot"]
	}
	
	def daftar_menu():
		print("=================================================")
		print("| kode\t|", "     daftar menu \t|", "harga \t|")
		print("=================================================")
		for i, menu_item in enumerate(menu):
		    print(f"|  {i+1} \t| {menu_item}      \t| {menu[menu_item]} \t|")
		print("=================================================")
	
	os.system("clear")	
	daftar_menu()
	
	while True:
	    beli = input("Pilih Menu(x untuk exit) : ")
	    if beli in list_menu:
	        break
	    elif beli == "x":
	    	print("progam berhenti")
	    	exit()
	    else:	
	    	print("Menu tidak tersedia. Silakan masukkan menu yang valid.")
	
	while True:
	    try:
	        jumlah = int(input("Jumlah Pesanan : "))
	        break
	    except ValueError:
	        print("Jumlah pesanan harus angka.")
	
	bayar = jumlah * list_menu[beli]
	
	if bayar > 60000:
	    diskon = bayar*10/100
	    total = bayar - diskon 
	else:
	    total = bayar 
	
	list_menu = {}
	for i, m in enumerate(menu.keys()):
	    list_menu[str(i+1)] = {m,}
	
	menu_pesanan = list_menu[beli]
	
	print("\n================= Detail Pembayaran =================")
	for item in menu_pesanan:
		print("Menu yang dipesan         : ",item)
	print("Jumlah yang dipesan       : ",jumlah)
	print("Total Biaya               : ",bayar)
	print("Total yang harus  dibayar : ",total)
	
	lanjut = input("\nlanjut berbelanja (Y/N)? ")
	if lanjut == "n":
		break
	else:
		continue