from boyer_more import boyer_more
import time

list = {
    "kaki 2": ["ayam", "gorila", "bebek", "elang", "burung unta"],
    "kaki 4": ["sapi", "kucing", "kambing", "anjing", "harimau", "rusa", "kuda", "gajah", "kuda nil"],
    "ekor": ["kucing", "harimau", "singa", "serigala", "buaya", "kadal", "ikan paus", "lumba-lumba"],
    "tanduk": ["banteng", "rusa", "kambing", "kerbau", "sapi", "kijang"],
    "sayap": ["ayam", "elang", "burung unta", "burung hantu", "kupu-kupu", "lebah", "nyamuk"],
    "sirip": ["ikan paus", "hiu", "lumba-lumba", "ikan pari", "ikan salmon", "ikan lele"],
    "bulu": ["ayam", "burung unta", "burung hantu", "elang", "bebek", "angsa", "penguin"],
    "sisik": ["buaya", "kadal", "ular"],
    "belalai": ["gajah"],
    "kantung": ["kanguru", "koala", "wombat"],
    "paruh": ["bebek", "angsa", "ayam", "burung hantu", "burung pipit"],
    "bisa": ["ular", "kalajengking", "lebah", "tawon"],
    "cakar": ["harimau", "singa", "kucing", "serigala", "elang", "ayam"],
    "kuku": ["kuda", "sapi", "kambing", "banteng"],
    "sirip punggung": ["hiu", "ikan paus", "ikan lele"],
    "penyengat": ["lebah", "tawon", "ubur-ubur"],
    "insang": ["ikan",]
}

def show_match(text, max_output = 5):
    print(f"{text}: \n{'-' * 20}")
    start_time = time.time()
    match = False
    output_count = 0

    for pattern, items in list.items():
        # print(pattern)
        position = boyer_more(text, pattern)
        if position != -1:
            match = True
            output = []
            for item in items:
                output.append(item)
                output_count += 1
                if output_count >= max_output: 
                    output_count = 0
                    break
            print(', '.join(output))
    if not match:
        print("not match found")

    end_time = time.time()
    duration = (end_time - start_time)
    print(f"{'-' * 20} \nAverage time: {duration:.10f} seconds\n\n")

if __name__ == "__main__":
    # hanya mencocokan text dengan pattern saja
    show_match("hewan berkaki 4")
    show_match("hewan berkaki 2")
    show_match("hewan yang memiliki sayap tetapi tidak bisa terbang")
    show_match("hewan bertanduk")
    show_match("mamalia berkaki 4 yang sering dipelihara")
    show_match("ikan yang hidup di laut")
    show_match("hewan memiliki tanduk yang kuat")

'''
======================================================= OUTPUT =======================================================\

hewan berkaki 4: 
--------------------
sapi, kucing, kambing, anjing, harimau
-------------------- 
Average time: 0.0000000000 seconds


hewan berkaki 2: 
--------------------
ayam, gorila, bebek, elang, burung unta
-------------------- 
Average time: 0.0000000000 seconds


hewan yang memiliki sayap tetapi tidak bisa terbang: 
--------------------
ayam, elang, burung unta, burung hantu, kupu-kupu
ular, kalajengking, lebah, tawon
-------------------- 
Average time: 0.0000000000 seconds


hewan bertanduk:
--------------------
banteng, rusa, kambing, kerbau, sapi
--------------------
Average time: 0.0000000000 seconds


mamalia berkaki 4 yang sering dipelihara:
--------------------
sapi, kucing, kambing, anjing, harimau
--------------------
Average time: 0.0011847019 seconds


ikan yang hidup di laut:
--------------------
not match found
--------------------
Average time: 0.0010113716 seconds


hewan memiliki tanduk yang kuat:
--------------------
banteng, rusa, kambing, kerbau, sapi
--------------------
Average time: 0.0000000000 seconds
'''