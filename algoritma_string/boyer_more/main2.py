import time

from boyer_more import boyer_more

if __name__ == "__main__":
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
        print(f"{text}: \n{'-' * 20}")
        match_set = []
        start_time = time.time()

        for pattern, items in list.items():
            position = boyer_more(text, pattern)
            if position != -1:
                match_set.append(set(items))

        print(f"found {len(match_set)} pattern: {match_set} \n===> ")
        if match_set:
            if len(match_set) > 1:
                common_items = set.intersection(*match_set)
            else:
                common_items = match_set[0]

            output_count = 0
            match = []
            for item in common_items:
                match.append(item)
                output_count += 1
                if output_count >= max_output:
                    break
            print(', '.join(match))
        else:
            print("no match found")


        end_time = time.time()
        duration = (end_time - start_time)
        print(f"{'-' * 20} \nAverage time: {duration:.10f} seconds\n\n")

    # mencocokan pattern namun jika terdapat 2 pattern akan dicari value yang sama
    show_match("hewan berkaki 4 yang hidup di hutan")
    show_match("hewan berkaki 2 yang bisa terbang")
    show_match("hewan berkaki 4 yang suka makan rumput")
    show_match("hewan berkaki 2 yang bisa memanjat")