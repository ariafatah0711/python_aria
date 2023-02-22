# looping dari list

# for loop
print("for loop")
kumpulan_angka = [4,3,2,5,6,4]

for angka in kumpulan_angka:
    print(f"angka: {angka}")

peserta = ["ucup", "otong", "dadang", "dudung"]

for nama in peserta:
    print(f"nama: {nama}")

# for loop dan range
print("\nfoor loop range")
kumpulan_angka = [10,5,6,4,3,5,3]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka {kumpulan_angka[i]}")

# while
print("\nwhile")
kumpulan_angka = [10,5,6,4,3,5,3]
print()

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka: {kumpulan_angka[i]}")
    i += 1

# list comperhension
print("\nlist comperhansion")
data = ["ucup", 1,2,3,"otong"]

[print(i) for i in data]

print()
[print(f"data: {i}") for i in data]

# enumerate
print("\nenumerate")
data_list = ["ucup", 1,2,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index: {index}, data: {data}")

## tambahan 
angka = [10,5,6,4,3,5,3]
angka_kuadrat = [i**2 for i in angka]

print(f"\nangka kuadarat dari angka: {angka_kuadrat}")