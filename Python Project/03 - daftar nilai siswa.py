# data
students = []
angka = 0
mean = 0

# menambahkan nama
while True:
    name = input("Masukkan nama siswa (ketik 'q' untuk keluar): ")
    if name == 'q':
        break

# menambahkan nilai        
    try:
        grade = int(input("Masukkan nilai siswa: "))
    except ValueError:
        print("Input nilai harus angka. Silakan coba lagi.")
        continue
    
    angka += 1
    mean += grade
    student = (angka, name, grade)
    students.append(student)

# hasil akhir
print("Data siswa:")
print("------------------------------------")
print("|NO | NAMA \t\t|  NILAI   |")
print("------------------------------------")

for student in students: 
    print("|", student[0], "|", student[1], "\t\t|", student[2], "\t   |")
    
print("------------------------------------")
mean = mean / angka
mean = round(mean, 1)
print("| * | nilai rata rata \t|", mean, "\t   |")
print("------------------------------------")