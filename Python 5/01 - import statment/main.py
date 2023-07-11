# import
# fungsinya untuk mengambil progam external / librery
# progam dari file external .py

# 1. untuk menyambung progam dari external
import external 
# maka dia akan menampilkan test yang telah fibuat di external.py

# 2. import dengan data
import variable
import data_def

# data ada di namespapce variable
''' print(data) # error '''
print(variable.data)

'''kesimpulan harus menambahkan nama file sebelum progam'''
data_def.fungsi("aria")

# import dengan fungsi
import matematika
hasil = matematika.tambah(4,5)

print(f"hasil: {hasil}")

