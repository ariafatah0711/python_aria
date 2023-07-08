# delete data list
data = ["nasi goreng", "telur", "ketoprak"]

del data[-1] # 1 artinya del data paling belakang
print(data)

# delete data set
user = {
    "aria":17,
    "zaki":16,
    "fadly":17
}

del user["zaki"]
print(user)

# angka awal : angka akhir : lompatanya
alfabet = ["a", "b", "c", "d", "e", "f"]

test_1 = alfabet[1:3]
print(test_1)

test_2 = alfabet[-3::] # artinya 3  kebelakang dari akhir akan di tampilkan sampai habis/0
print(test_2)

test_3 = alfabet[-3::2]
print(test_3)

test_4 = alfabet[0:5:2]
print(test_4)

test_5 = alfabet[::2]
print(test_5)

#####################
test_6 = alfabet[2:-1:1] # kesimpulanya index 2 k3 index negatif 1 dan lompatanya akan defult menjadi 1
print(test_6)

test_7 = alfabet[-2:1:] # kosong dikarenakan tidak adanya lompatan karena disini urutanya negatif / dari akhir
print(test_7) # maka jika dari akhir namun lompatanya 1 tidak akan dapat menghasilkan apapun

test_7 = alfabet[-2:1:-1] # bebeda dengan ini yang akan tampil karena lompatanya -1/ dari akhir ke awal
print(test_7)