'''type hints untuk fungsi'''

# bentuk standar fungsi yang kita pelajari
'''
def fungsi(parameter):
    print(parameter)

fungsi(1)
fungsi("ucup")
fungsi(True)
'''

# type hints
# penggunaan ytpe hints 
'''fungsi(parameter:type_data=defaul_tvalue):'''

# arti dati -> int adalah parameter harus int dan output akan int
# jika kita tidak menambahakan -> keteranganya akan menjadi int -> any
def fungsi_dengan_hints(parameter:int) -> int:
    output = 10**parameter
    return output

hasil_2 = fungsi_dengan_hints(2)
print(hasil_2)

'''
hasil_str = fungsi_dengan_hints("aria")
print(hasil_str)'''
# erorr jika pake str

# string
import string
def display(parameter:string):
    print(parameter)

display("ucup")

# (function) def system(command: StrOrBytesPath) -> int
import os
hasil = os.system("cls")
print(hasil)
# penyebab tidak berhasil karena function os system tidak di return

