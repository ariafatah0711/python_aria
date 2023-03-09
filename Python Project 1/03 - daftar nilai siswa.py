import os

# data
students = []
angka = 0
mean = 0

# menambahkan nama
while True:
    os.system("clear")
    name = input("\033[36;1mMasukkan nama siswa \033[32;1m(ketik 'q' untuk keluar): \033[37;1m")
    if name == 'q':
        break

# menambahkan nilai        
    try:
        grade = int(input("\n\033[36;1mMasukkan nilai siswa: \033[37;1m"))
    except ValueError:
        print("\033[31;1mInput nilai harus angka. Silakan coba lagi.")
        continue
    
    angka += 1
    mean += grade
    student = (angka, name, grade)
    students.append(student)


# hasil akhir
os.system("clear")
print(f"\033[36;1m{'DATA SISWA':^44}")
print("\033[33;1m-"*44)
print("|NO | NAMA \t\t\t|  NILAI   |")
print("-"*44)

for student in students: 
    print("|", student[0], "|\033[36;1m", student[1], "\t\t\t\033[33;1m|\033[32;1m", student[2], "\t   \033[33;1m|")
    
print("-"*44)
mean = mean / angka
mean = round(mean, 1)
print("| * | nilai rata rata \t\t|\033[32;1m", mean, "\t   \033[33;1m|")
print("-"*44, "\033[37;1m")