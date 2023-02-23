# list -> array, mengakses data menggunakan index

data_list = ["ucup", "otong"]
print(data_list[0], "\n")

# Dictionary (dict) -> associative array
# identifier

data_dict = {
    "key1":"value1",
    "key2":"value2",
    "cp":"ucup",
    "nomer":100,
    100:"seratus",
    "list":data_list
}

print(data_dict)
print(data_dict["cp"])
print(data_dict["nomer"])
print(data_dict[100])
print(data_dict["list"])

# operasi Dicitonary

data_dict = {
    "cup":"ucup ganteng",
    "tong":"otong ga ganteng",
    "dung":"gundung gundul"
}

# panjang dictionary
lendict = len(data_dict)
print(f"\npanjang dictionary: {lendict}")

# mengeck key exist atau tidak
key = "cup"
checkkey = key in data_dict
print(f"apakah {key} ada di dalam data_dict: {checkkey}")

# mengakses value (read), dengan get
print(data_dict["cup"]) # pake [] saat tanpa menggunakan get
print(data_dict.get("cup")) # pake () saat pake get
print(data_dict.get("kiss", "key tidak ditemukan"))

# fungsinya agar jika tidak ada key kiss di dictionary dia tidak akan error dan hanya mengeluarkan output none

# mengupdate data
data_dict["cup"] = "ucup keren abizzzz"
print("\n", data_dict)

# menambah data
data_dict["sep"] = "asep si paling ngoding"
print("\n", data_dict)

# agar simpple menggunakan .update
# harus gunakan ({key:value})
data_dict.update({"cup":"ucup ganteng"})
print("\n", data_dict)
data_dict.update({"ar":"aria gantenggggggggggg"}) # jika key tidak ada dia akan meng add baru
print("\n", data_dict)

# menhapus data dict
del data_dict["ar"]
print("\n", data_dict)
