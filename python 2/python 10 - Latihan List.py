# progam list buku

list_buku = []

while True:
    print("\nmasukan data buku")
    judul = input("masukan judul buku \t: ")
    penulis = input("masukan nama penulis\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\nNo. \t| Judul\t\t| Penulis")
    print("-"*35)
    for index,buku in enumerate(list_buku):
        print(f"{index+1}.\t| {buku[0]}  \t| {buku[1]}")

    print("-"*35)
    lanjut = input("apakah anda mau lanjut?(Y/N) ")

    if lanjut == "n":
        break

print("\nprogam selesai")

