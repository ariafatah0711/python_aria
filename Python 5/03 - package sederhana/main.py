import time
t_start = time.time()

# package
import sains.matematika
from sains import fisika # arrtinya mengambil file pisika dari folder sains tanpa memilih sains
from sains.fisika import gaya as v# artinya dari folder sains. dan file fisika mengambil gaya

hasil_tambah = sains.matematika.tambah(2,3,5,10) 
print(f"hasil tambah fari pcakage: {hasil_tambah}")

gaya = fisika.gaya(90, 10)
print(f"gaya adalah: {gaya}")

gaya = v(90, 12)
print(f"gaya adalah: {gaya}")

t_end = time.time()
print(f"waktu eksekusi adalah {t_end - t_start}")