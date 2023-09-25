# Matplotlib => library untuk melakukan visualisasi data.
import matplotlib.pyplot as plt
 
# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
 
# Membuat plot garis
plt.plot(x, y)
 
# Menambahkan judul dan label sumbu
plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
 
# Menampilkan plot
plt.show()