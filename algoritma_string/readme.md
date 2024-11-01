# pencocokan string
- T (Text) => string yang relativ panjang
    - dengan panjang karakter n
    - ex: "SAYA ALIEN"
- P (Patern) => string yang akan di cocokan dengan T
    - dengan panjang karakter m (asumsi m <<< n) yang akan dicari di dalam text
    - ex: "ALI"

## string concept
- string => rangkain / larik dengan tiap elemen adalah karakter
    - misal sebuah string S dengan panjang karakter m
    - S = x⁰x¹x²...Xm-1
        andrew = 012345

## prefix (awalan)
- awalan dari sebuah string yang merupakan bagian dari sub string yang harus diawali di index 0 dan berakhir di index k
    - k = suatu index antara 0 hingga m-1
    - Substring => S [0..k]
    - ex: T = andrew
        - k = 0, a
        - l = 1, an
        - a. an. and. adr, adre, andrew

## suffix (akhiran)
- akhiran dari sebuah string ....
    - k = suatu index antara 0 hingga m-1
    - Substring => [k..m-1]
    - ex: T = andrew
        - k = 0, w
        - k = 1, e

# algoritma
## algoritma brute force
- memeriksa satu persatu setiap karakter pada T apakah match dengan karakter pada P
- jika berbeda P akan mulai bergeeser 1 karakter di T
- ex
    - T : SAYA ALIEN
    - P : ALI
    - ........
        - 1
            - T : S
            - P : A (tdk cocok Text akan bergeser 1 ke kanan)
        - 2
            - T : SA
            - P :  A (cocok dan pattern akan bergeser)
        - 3
            - T : SAY
            - P :  AL (tdk cocok Pattern akan kembali ke index 0, dan Text akan bergeser ke kiri)
        - ...
            - T : SAYA
            - P :   A (dan seterusnya)

- kasus terburuk
        - ketika karakter awal pada pattern namun karakter terakhir berbeda pada text
            - sehingga kita mengulangi pemeerriksaan yang sama
        - ex: T: aaaaaaah p: aah
    
- kasus terbaik
        - ketika dari awal textt pattern meendapatkan karakter yang berbeda di karakter pertamnya
            - jadi tidak perlu mengulangin lagi
        - ex: T: sukabanget P: get

- analisis
        - pendekatan brute force cukup cepat ketika jenis karakter dari text dan pattern sangat beragam
            - ex: A..Z, a..z, 1..9, dll
        - pendekatan brute force akan lambat ketika jenis karakter pada text dan pattern tidak beragam
            - ex: 0, 1 (dalam binary files, images file, dll)

## algoritma KMP (Knuth-Morris-Pratt)
- mirip dengan algoritma brute force yang melakukan peergeseran dari kiri ke kanan
- pergeseran yang dilakukan lebih cerdas daripada bruteforce
    - menggunakan konsep prefix, dan suffix
        - prefix (awalan) S [0..k]
        - suffix (akhritan) S [k..m-1]
        - k = suatu index antara 0 hingga m-1
    - mempertimbangkan sebnyak mungkin pergeseran
        - tidak mengulang pemeriksaan yang sama 

- ketika terjadi mismatch maka pergeseran yang dilakukan 
    - adalah sebnayak nilai prefix P [0..j-1] terbesar
    - yang juga merupakan suffix P[1..j-1]

- ex:
    T : abaabx
        111110
    p : abaaba
    - ketika terjadi mismatch pada index 6, maka pergeseran yang dilakukan adalah sebanyak j = 5
        - prefix: a, ab, aba, abaa, abaab
        - suffix: b, ab, aab, baab
    - prefix dan suffix yang sama adalah ab
        - nilai 2 artinya index P yang diperiksa mulai dari index ke -2
        - dan pergeseran akan dikurangi 2
    - ...
        - 1
            T : abaabx
                111110
            p : abaaba (j = 5)
        - 2
            T : abaabx
                   110
            p :    abaaba (j = 2)

