# read = r
# write = w

# 1. mode write
# dia akan membuat file baru jika tidak ada file nya
# dan akan menimpa file

with open("data_1.txt", "w", encoding="utf-8") as file: # akan otomatis membuat data_1.txt
    file.write("jon si jhony") # untuk menulis

with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("ucup su rucup")

    # jony si jhony akan tertimpa

# 2. mode append = a
with open("data_2.txt", "w", encoding="utf-8") as file: # w write
    file.write("jon si jhony\n")

    # semisal data_2 sudah memiliki 3 baris, dan yang atas adalah a semua maka 
    # 3 baris seblumnya akan di
    # append dengan baris baris lagi menjadi 6 baris ....  dan seterusnya

with open("data_2.txt", "a", encoding="utf-8") as file: # a append
    file.write("aria fatah ganteng banget\n")

with open("data_2.txt", "a", encoding="utf-8") as file: # a append
    file.write("tambah lagi dengan append\n")

# 3. mode r+

with open("data_3.txt", "w", encoding="utf-8") as file: # a append
    file.write("data ke-3\n")

# bisa read dan write
# with open di atas akan tertimpa karena mode r+ memiliki fungsi write juga

# 1. dapat membuat baris dan di read
with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("baris ke 1\n")
    file.write("baris ke 2\n")
    file.write("baris ke 3\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    data = file.read()
    print(f"data file_1 pada r+ \n{data}")

# 2. baris 1 jika di ubah tidak berpengaruh yang lainya
with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("ariaa ke 1\n") # ini adalah baris 1 dan ditimpa
    # baris 2 tidak kenapa napa karena ini adalah read +