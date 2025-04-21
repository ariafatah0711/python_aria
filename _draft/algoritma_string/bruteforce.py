def brute(text, pattern):
    # panjang text dan pattern
    t = len(text)
    p = len(pattern)

    for i in range(t - p + 1):
    # looping sebanyak panjang text - patttern ditambah 1 (26 - 5 + 1) = 22
        j = 0 
        # index pattern
        while j < p and text[i + j] == pattern[j]:
            # mencoba mencocokan text[0] + j (0) dengan patern[j]
            # jika tidak cocok akan dilewati
                # ketika cocok maka j ditambah 1 text[13] + j (0) dengan pattern[j] (0)
                # lalu ketika mencocokan text[14] + j (1) dengan pattern [j] (1)
                    # dan ternyata tidak cocok akan di cocokan kembali dari awal
                # cocok ketika sampai di index ke t(15, 16, 17, 18) dengan pattern dengan index j(0,1,2,3)
            j += 1
        if j == p:
            return i # pola ditemukan
    return - 1

text = "aku suka makan nasi goreng"
# 012 4567 9.10,11,12,13 14,15,16...

pattern = "nasi"
result = brute(text, pattern)
print(result) # result 15

pattern = "nasi a"
result_salah = brute(text, pattern)
print(result_salah) # result -1

pattern = "gorenx"
# karena text akan dihitung sebanyak jumlah text - pattern + 1 maka akan melakukan pengencekan sampai jumlah pattern yang diakhir + 1 saja
# karena ketika sudah sampai situ text lanjutanya akan dibaca lagi di while j nya
result_salah = brute(text, pattern)
print(result_salah) # result -1


################## templatte ##############################
def template(text, pattern):
    t = len(text)
    p = len(pattern)

    for i in range(t - p + 1):
        j = 0 
        while j < p and text[i + j] == pattern[j]:
            j += 1
        if j == p:
            return i
    return - 1