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
    lps = compute_lps(pattern) # nanas [0,0,0,0,0] => [0,0,1,2,0]
    i = 0 # for text
    j = 0 # for pattern
    while i < len(text):
        # looping jika i lebih kecil dari panjang text
        if pattern[j] == text[i]:
            # jika pattern dan text sama maka index akan ditambah
            i += 1
            j += 1
        if j == len(pattern):
            # jika j sama dengan panjang pattern maka pattern ditemukan
            print(f"pattern ditemukan di {i - j}")
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            # jika i lebih kecil dari panjang text dan pattern si j bukan sama dengan text i
            if j != 0:
                # dan j tidak sama dengan 0 maka j akan menjadi  angka lps[j-1]
                # kita tidak perlu menghitung dari awal lagi
                j = lps[j - 1]
            else:
                i += 1

text = "nani dan nana makan nanas"
# 0,1,2,3 5,6,7 9,10,11,12 14,15,16,17,18 20,21,22,23,24
pattern = "nanas"
kmp(text, pattern)
print("")

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp(text, pattern)
print("")

text = "101010100010101010101010101010010101001010101"
pattern = "101010010"
kmp(text, pattern)