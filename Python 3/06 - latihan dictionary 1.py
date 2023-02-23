import datetime, os, random, string

# template dict mahasiswa
mahasiswa_template = {
    "nama":"nama",
    "nim":"0000000",
    "sks_lulus":0,
    "lahir":datetime.datetime(1111,11,1)
}

# data kosong
data_mahasiswa = {}

# while true agar berulang
while True:
    # clear
    os.system("clear") # untuk menjalankan terminal

    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    # data kosong menggunakan dict.fromkeys
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    # input 
    mahasiswa["nama"] = input("nama_mahasiswa: ")
    mahasiswa["nim"] = input("nim mahasiswa: ")
    mahasiswa["sks_lulus"] = int(input("sks lulus: "))

    # tahun lahir
    tahun_lahir = int(input("tahun lahir (YYYY): "))
    bulan_lahir = int(input("bulan lahir (1-12): "))
    tanggal_lahir = int(input("tanggal lahir (1-31): "))
    mahasiswa["lahir"] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

    # menambahkan data mahasiswa yg diinput ke dalam data_mahasiswa
    # artinya kita bikin key dgn random memilih string, dgn code nya asci falam 6x
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    # dari tutorial sebelumnya hilangkan beasiswa
    # output
    print(f"\n{'key':<6} {'nama':<17} {'nim':<13} {'sks lulus':<10} {'tanggal lahir':<10}")
    print("-"*64)

    for mahasiswa in data_mahasiswa:
        key = mahasiswa

        nama = data_mahasiswa[key]["nama"]
        nim = data_mahasiswa[key]["nim"]
        sks = data_mahasiswa[key]["sks_lulus"]
        lahir = data_mahasiswa[key]["lahir"].strftime("%x")

        print(f"{key:<6} {nama:<17} {nim:<13} {sks:^10} {lahir:^10}")

    is_done = input("\nlanjut(Y/N)? ")
    if is_done == "n":
        break

print("\nakhir dari progam terima kasih.")