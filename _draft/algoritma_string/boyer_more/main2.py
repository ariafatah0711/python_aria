import time
from boyer_more import boyer_more

list = {
    # Ciri-ciri hewan
    "kaki 2": ["ayam", "bebek", "gorila", "burung", "angsa"],
    "kaki 4": ["sapi", "harimau", "serigala", "kucing", "gajah", "rusa", "kambing", "kuda", "anjing", "kerbau"],
    "bulu": ["ayam", "bebek", "burung", "angsa", "penguin"],
    "bersisik": ["ikan", "buaya", "kadal"],
    "cangkang": ["kura-kura", "siput"],

    # Tempat tinggal hewan
    "hutan": ["gorila", "serigala", "kucing", "harimau", "rusa", "gajah", "kancil"],
    "air": ["ikan", "buaya", "katak", "penyu"],
    "gurun": ["unta", "kadal"],
    "udara": ["burung", "kelelawar"],

    # Kemampuan
    "berenang": ["ikan", "katak", "buaya", "penyu", "berang-berang"],
    "terbang": ["burung", "kelelawar", "angsa", "elang"],
    "memanjat": ["kucing", "monyet", "gorila"],
    "berlari cepat": ["cheetah", "rusa", "kuda", "serigala"],

    # makanan
    "rumput": ["sapi", "kuda", "rusa", "kerbau", "zebra"]
}

def show_match(text, max_output = 5):
    print(f"text \t\t: {text}: \n{'-' * 40}")
    match_set = []
    match_pattern = []
    start_time = time.time()

    for pattern, items in list.items():
        position = boyer_more(text, pattern)
        if position != -1:
            match_set.append(set(items))
            match_pattern.append(pattern)

    # print(f"found {len(match_set)} pattern: {match_set} \n===> ")
    match_set_fil = ', '.join([f"{{{', '.join(sorted(match))}}}" for match in match_set])
    print(f"found {len(match_set)} pattern\t: {', '.join(match_pattern)}  \nvalue pattern \t: {match_set_fil} \n{'-' * 40} ")

    if match_set:
        if len(match_set) > 1:
            common_items = set.intersection(*match_set)
        else:
            common_items = match_set[0]

        output_count = 0
        match = []
        if common_items:
                for item in common_items:
                    match.append(item)
                    output_count += 1
                    if output_count >= max_output:
                        break
        else:
            for items in match_set:
                if items:
                    match.append(next(iter(items)))
                    if len(match) >= max_output:
                        break
        print(f"value output \t: {', '.join(match)}")
    else:
        print("no match found")


    end_time = time.time()
    duration = (end_time - start_time)
    print(f"Average time \t: {duration:.10f} seconds\n\n")

if __name__ == "__main__":
    # mencocokan pattern namun jika terdapat 2 pattern akan dicari value yang sama
    show_match("hewan berkaki 4 yang hidup di hutan") # 2 pattern
    show_match("hewan berkaki 2") # 1
    show_match("hewan berkaki 4 yang suka makan rumput yang hidup di hutan") # 3
    show_match("hewan yang memiliki ekor dan bisa memanjat serta terbang") # 2 tapi valuenya gak sama
    
'''
======================================================= OUTPUT =======================================================

text            : hewan berkaki 4 yang hidup di hutan: 
----------------------------------------
found 2 pattern : kaki 4, hutan  
value pattern   : {anjing, gajah, harimau, kambing, kerbau, kucing, kuda, rusa, sapi, serigala}, {gajah, gorila, harimau, kancil, kucing, rusa, serigala} 
---------------------------------------- 
value output    : serigala, gajah, rusa, harimau, kucing
Average time    : 0.0009975433 seconds


text            : hewan berkaki 2: 
----------------------------------------
found 1 pattern : kaki 2  
value pattern   : {angsa, ayam, bebek, burung, gorila} 
---------------------------------------- 
value output    : gorila, bebek, burung, ayam, angsa
Average time    : 0.0000000000 seconds


text            : hewan berkaki 4 yang suka makan rumput yang hidup di hutan: 
----------------------------------------
found 3 pattern : kaki 4, hutan, rumput  
value pattern   : {anjing, gajah, harimau, kambing, kerbau, kucing, kuda, rusa, sapi, serigala}, {gajah, gorila, harimau, kancil, kucing, rusa, serigala}, {kerbau, kuda, rusa, sapi, zebra} 
---------------------------------------- 
value output    : rusa
Average time    : 0.0010011196 seconds


text            : hewan yang memiliki ekor dan bisa memanjat serta terbang:
----------------------------------------
found 2 pattern : terbang, memanjat
value pattern   : {angsa, burung, elang, kelelawar}, {gorila, kucing, monyet}
----------------------------------------
value output    : angsa, kucing
Average time    : 0.0009994507 seconds
'''