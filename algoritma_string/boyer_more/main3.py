import time
from boyer_more import boyer_more
import pandas as pd

# read data excel
file = "data-2.xlsx"
df = pd.read_excel(file, usecols=['pattern', 'value', 'test']) 
# print(df)

data_dict = df.set_index('pattern')['value'].to_dict()
data_dict = {key.lower(): value.lower().split(', ') for key, value in data_dict.items()}
list = data_dict
# print(list)

def show_match(text, max_output = 5):
    print(f"text \t\t: {text}: \n{'-' * 40}")
    text = text.lower()
    match_set = []
    match_pattern = []
    start_time = time.time()

    for pattern, items in list.items():
        position = boyer_more(text, pattern)
        if position != -1:
            match_set.append(set(items))
            match_pattern.append(pattern)

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
    # show_match("hewan berkaki 4 yang hidup di hutan")
    # show_match("hewan berkaki 2 yang bisa terbang")
    # show_match("hewan berkaki 4 yang suka makan rumput")
    # show_match("hewan berkaki 2 yang bisa memanjat")
    
    show_match("authentication default login") # 1 pattern
    show_match("authentication default website") # 2 tapi gak ada yang sama
    show_match("my wifi got arp spoofing") # 2 tapi gak ada yang sama
    pass


'''
======================================================= OUTPUT =======================================================
text            : authentication default login: 
----------------------------------------
found 1 pattern : authentication  
value pattern   : {enforce multi-factor authentication, implement account lockout, password default cred} 
---------------------------------------- 
value output    : enforce multi-factor authentication, implement account lockout, password default cred
Average time    : 0.0005803108 seconds


text            : authentication default website: 
----------------------------------------
found 2 pattern : authentication, web  
value pattern   : {enforce multi-factor authentication, implement account lockout, password default cred}, {implement content security policy (csp), sanitize user input to prevent xss} 
---------------------------------------- 
value output    : enforce multi-factor authentication, sanitize user input to prevent xss
Average time    : 0.0000000000 seconds


text            : my wifi got arp spoofing: 
----------------------------------------
found 2 pattern : wifi, spoofing  
value pattern   : {enable 5ghz wifi, secure wi-fi with wpa3}, {implement dhcp snooping, set disable automation arp or arp-reply only} 
---------------------------------------- 
value output    : enable 5ghz wifi, implement dhcp snooping
Average time    : 0.0000000000 seconds

'''