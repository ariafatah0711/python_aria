def kmp(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = 0  # indeks untuk text
    j = 0  # indeks untuk pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j  # posisi di mana pattern ditemukan
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1  # tidak ditemukan

# if __name__ == "__main__":
#     print("=== DEMO ALGORITMA BRUTE FORCE MATCHING ===")
#     text = "hewan berkaki 2"
#     pattern = "kaki 2"
#     print(f"[*] Text    : {text}")
#     print(f"[*] Pattern : {pattern}")

#     def kmp(text, pattern):
#         def compute_lps(pattern):
#             lps = [0] * len(pattern)
#             length = 0
#             i = 1

#             print("\n[=] Membangun LPS Array:")
#             print(f"    Pattern: {pattern}")
#             while i < len(pattern):
#                 if pattern[i] == pattern[length]:
#                     length += 1
#                     lps[i] = length
#                     print(f"    lps[{i}] = {length} (karena '{pattern[i]}' == '{pattern[length - 1]}')")
#                     i += 1
#                 else:
#                     if length != 0:
#                         length = lps[length - 1]
#                         print(f"    Mismatch, mundur ke lps[{length}]")
#                     else:
#                         lps[i] = 0
#                         print(f"    lps[{i}] = 0 (karena tidak cocok dan length = 0)")
#                         i += 1
#             print(f"    Hasil LPS: {lps}\n")
#             return lps

#         lps = compute_lps(pattern)
#         i = 0  # indeks untuk text
#         j = 0  # indeks untuk pattern

#         print("[=] Proses Pencocokan:")
#         while i < len(text):
#             print(f"    Cek text[{i}]='{text[i]}' vs pattern[{j}]='{pattern[j]}'")
#             if pattern[j] == text[i]:
#                 i += 1
#                 j += 1
#                 print(f"    Cocok, lanjut i={i}, j={j}")
#             if j == len(pattern):
#                 print(f"\n[✓] Pattern ditemukan pada index {i - j}!\n")
#                 return i - j  # posisi di mana pattern ditemukan
#             elif i < len(text) and pattern[j] != text[i]:
#                 print(f"    Tidak cocok.")
#                 if j != 0:
#                     j = lps[j - 1]
#                     print(f"    Kembali ke j={j} (dari LPS)")
#                 else:
#                     i += 1
#                     print(f"    Geser i ke {i}")
#         print("\n[✗] Pattern tidak ditemukan.\n")
#         return -1

#     kmp(text.lower(), pattern.lower())