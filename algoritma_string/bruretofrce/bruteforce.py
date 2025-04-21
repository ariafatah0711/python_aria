def bruteforce(text, pattern):
    t = len(text)
    p = len(pattern)

    for i in range(t - p + 1):
        j = 0 
        while j < p and text[i + j] == pattern[j]:
            j += 1
        if j == p:
            return i
    return - 1

if __name__ == "__main__":
    print("=== DEMO ALGORITMA BRUTE FORCE MATCHING ===")
    text = "hewan berkaki 4 yang hidup di hutan"
    pattern = "kaki 4"

    print(f"Teks     : {text}")
    print(f"Pattern  : {pattern}")
    print("\nLangkah-langkah pencocokan:")

    t = len(text)
    p = len(pattern)

    for i in range(t - p + 1):
        print(f"\n[+] Cek mulai dari indeks {i}:")
        j = 0
        while j < p and text[i + j] == pattern[j]:
            print(f"    Cocok: text[{i + j}] == pattern[{j}] -> {text[i + j]} == {pattern[j]}")
            j += 1
        if j < p:
            if i + j < len(text):
                print(f"    Gagal: text[{i + j}] != pattern[{j}] -> {text[i + j]} != {pattern[j]}")
            else:
                print("    Gagal: indeks melampaui batas teks")
        if j == p:
            print(f"\n[*] Pattern cocok di indeks ke-{i}")
            break
    else:
        print("\n[*] Pattern tidak ditemukan.")