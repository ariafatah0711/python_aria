class last_onccurence(object):
    def __init__(self, pattern, alphabet):
         self.occurrences = dict()
         for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)
    def __call__(self, letter):
        return self.occurrences[letter]

def boyer_more(text, pattern):
    
    alphabet = set(text)
    last = last_onccurence(pattern, alphabet)
    t = len(text)
    p = len(pattern)
    i = p - 1
    j = p - 1
    
    while i < t:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + p - min(j, 1 + l)
            j = p - 1
    return -1

if __name__ == "__main__":
    print("=== DEMO ALGORITMA BOYER-MOORE (Last Occurrence) ===")
    text = "hewan berkaki 4 yang hidup di hutan"
    pattern = "kaki 4"

    print(f"Teks     : {text}")
    print(f"Pattern  : {pattern}")
    print("\nLangkah-langkah pencocokan:")

    alphabet = set(text)
    last = last_onccurence(pattern, alphabet)
    t = len(text)
    p = len(pattern)
    i = p - 1
    j = p - 1

    step = 1
    while i < t:
        print(f"\n[Step {step}] Bandingkan text[{i}] = '{text[i]}' dengan pattern[{j}] = '{pattern[j]}'")
        if text[i] == pattern[j]:
            if j == 0:
                print(f"--> Cocok! Pola ditemukan di indeks {i}")
                break
            else:
                i -= 1
                j -= 1
                print(f"    Karakter cocok, geser ke kiri: i = {i}, j = {j}")
        else:
            l = last(text[i])
            shift = p - min(j, 1 + l)
            print(f"    Karakter tidak cocok.")
            print(f"    Last occurrence '{text[i]}' di pattern = {l}")
            print(f"    Geser indeks i sebanyak {shift} langkah ke kanan.")
            i = i + shift
            j = p - 1
        step += 1
    else:
        print("\n[*] Pattern tidak ditemukan.")