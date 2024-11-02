from boyer_more import boyer_more
import time

if __name__ == "__main__":
    list = {
        "kaki 2": ["ayam", "gorila", "bebek", "elang", "burung unta"],
        "kaki 4": ["sapi", "kucing", "kambing", "anjing", "harimau", "rusa", "kuda", "gajah", "kuda nil"],
        "ekor": ["kucing", "harimau", "singa", "serigala", "buaya", "kadal", "ikan paus", "lumba-lumba"],
        "tanduk": ["banteng", "rusa", "kambing", "kerbau", "sapi", "kijang"],
        "sayap": ["ayam", "elang", "burung unta", "burung hantu", "kupu-kupu", "lebah", "nyamuk"],
        "sirip": ["ikan paus", "hiu", "lumba-lumba", "ikan pari", "ikan salmon", "ikan lele"],
        "bulu": ["ayam", "burung unta", "burung hantu", "elang", "bebek", "angsa", "penguin"],
        "sisik": ["buaya", "kadal", "ular", "ikan lele", "ikan gurame", "ikan pari"],
        "belalai": ["gajah"],
        "kantung": ["kanguru", "koala", "wombat"],
        "paruh": ["bebek", "angsa", "ayam", "burung hantu", "burung pipit"],
        "bisa": ["ular", "kalajengking", "lebah", "tawon"],
        "cakar": ["harimau", "singa", "kucing", "serigala", "elang", "ayam"],
        "kuku": ["kuda", "sapi", "kambing", "banteng"],
        "sirip punggung": ["hiu", "ikan paus", "ikan lele"],
        "penyengat": ["lebah", "tawon", "ubur-ubur"],
        "insang": ["ikan lele", "ikan gurame", "ikan pari", "ikan hiu", "ikan koi"]
    }

    def show_match(text, max_output = 2):
        print(f"{text}:")
        start_time = time.time()
        repeat = 1
        match = False
        output_count = 0

        for pattern, animals in list.items():
            # print(pattern)
            position = boyer_more(text, pattern)
            if position != -1:
                match = True
                for v in animals:
                    print(v)
                    output_count += 1
                    if output_count >= max_output: 
                        output_count = 0
                        break
        if not match:
            print("not match found")

        end_time = time.time()
        # duration_time = end_time - start_time
        duration = (end_time - start_time) / repeat
        print(f"Average time per match search: {duration:.10f} seconds\n")

    show_match("sapi hewan berkaki 4")
    show_match("ayam hewan berkaki 2")
    show_match("kucing hewan berkaki 4")
    show_match("banteng hewan bertanduk")
    show_match("sapi merupakan mamalia berkaki 4 yang sering dipelihara")
    show_match("ikan hiu adalah ikan yang hidup di laut")
    show_match("banteng memiliki tanduk yang kuat")
    show_match("penguin adalah burung yang memiliki sayap tetapi tidak bisa terbang")
