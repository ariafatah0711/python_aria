import time
from boyer_more import boyer_more
import pandas as pd

# data spredsheet
file = "data-3.xlsx"
row = ["pattern", "value", "priority"]
# df = pd.read_excel(file, usecols=row) # default
df = pd.read_excel(file, usecols=row).sort_values(row[2]).reset_index(drop=True) # sort value by priority and reset index
print(df)

def main(text):
    print(f"[*] text \t: {text}")
    patterns, match, match_same = [], [], []
    
    for index, row in df.iterrows():
        pattern = row['pattern']
        position = boyer_more(text.lower(), pattern.lower())
        if (position != -1):
            value = row["value"]
            # priority = row['priority']
            if pattern not in patterns:
                patterns.append(pattern)
            if value in match:
                match_same.append(value)
            else:
                match.append(value)

    if (len(match_same) != 0):
        print(f"[+] beberapa pattern ditemukan ({', '.join(patterns)})")
        print(f"[+] value yang sama ditemukan!")
        print(f"[ ] value \t: {', '.join(match_same)} \n")
    else:
        print(f"[+] pattern ditemukan ({', '.join(patterns)})")
        print(f"[+] value yang sama tidak ditemukan!")
        print(f"[ ] value \t: {', '.join(match)} \n")

if __name__ == "__main__":
    # main program
    main("hewan berkaki 2") # kaki 2 (akan menampilkan semua value dengan priority tertinggi terlebih dahulu)
    main("hewan berkaki 4 yang hidup di hutan") # kaki 4, hutan true(akan menampilkan value yang sama pada beberapa pattern, jika tidak ada value yang sama maka akan menampilkan semua value)
    main("hewan berkaki 2 yang suka makan rumput") # kaki 2, rumput false(akan menampilkan value yang sama pada beberapa pattern, jika tidak ada value yang sama maka akan menampilkan semua value)
    
    # main("found 1 found 2")
    # main("found 2 found 3")

'''
Prioritas 1: Hewan yang umum atau sering dilihat dalam kategori tersebut.
Prioritas 2: Hewan yang cukup umum dalam kategori tersebut.
Prioritas 3: Hewan yang kurang umum dalam kategori tersebut.
Prioritas 4: Hewan yang cukup langka atau memiliki karakteristik spesial dalam kategori tersebut.
Prioritas 5: Hewan yang sangat jarang atau unik dalam kategori tersebut.

          pattern    value  priority
0          kaki 2     ayam         1
1         found 1  value 2         1
2         found 1  value 1         1
3          Rumput     sapi         1
4        Memanjat   kucing         1
..            ...      ...       ...
60           bulu  penguin         5
61            Air    penyu         5
62  Berlari Cepat  cheetah         5
63         kaki 4    gajah         5
64          Hutan    gajah         5

[65 rows x 3 columns]
[*] text        : hewan berkaki 2
[+] pattern ditemukan (kaki 2)
[+] value yang sama tidak ditemukan!
[ ] value       : ayam, bebek, burung, angsa, gorila

[*] text        : hewan berkaki 4 yang hidup di hutan
[+] beberapa pattern ditemukan (Hutan, kaki 4)
[+] value yang sama ditemukan!
[ ] value       : kucing, rusa, serigala, harimau, gajah

[*] text        : hewan berkaki 2 yang suka makan rumput
[+] pattern ditemukan (kaki 2, Rumput)
[+] value yang sama tidak ditemukan!
[ ] value       : ayam, sapi, bebek, kerbau, kuda, burung, angsa, rusa, gorila, zebra
'''