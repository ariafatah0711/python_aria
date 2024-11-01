lps = [0] * len("aria")
print(lps, "\n")

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0 # panjang awalan yang tidak cocok
    # jika pattern ababc: [0,0,1,2,0]
    i = 1

    while i < len(pattern):
        # perulangan i (1) < 5
        # print(f"=>", pattern[i], pattern[length])
        print(f"=> {pattern[i]} {pattern[length]} | index pattern {i} == {length}")
        if pattern[i] == pattern[length]:
        # jika pattern[1] sama pattern[0]
        # a, n, n, n (2, 1)
            length += 1
            # ketika n == n length akan ditambah 1
            lps[i] = length
            # dan lps index ke 2 akan menjadi 1
            i += 1
            print(length, lps)
        else:
            if length != 0:
                # ketika length bukan 0
                length = lps[length - 1]
                # length akan menjadi lps
                print(length, lps)
            else:
                lps[i] = 0
                # ketika tidak cocok lps[i] akan ubah jadi 0
                i += 1
                print(length, lps)
    return lps
                
                
pattern = "nanas"
lps = compute_lps(pattern) # nanas [0,0,0,0,0] => [0,0,1,2,0]
print(lps, "\n")

pattern = "ABABCABAB"
lps = compute_lps(pattern) # [0,0,0,0,0,0,0,0] => [0,0,1,2,0,1,2,3,4]
print(lps, "\n")