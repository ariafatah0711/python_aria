import time
from bruteforce import bruteforce
import pandas as pd
from pathlib import Path

# data spredsheet
file = Path(__file__).parent / "../data.xlsx"
row = ["pattern", "value"]

df = pd.read_excel(file, usecols=row)
# print(df)

def main(text):
    start = time.perf_counter()
    print(f"[*] text \t: {text}")
    patterns, match, match_same = [], [], []

    for _, row in df.iterrows():
        pattern = row['pattern']
        position = bruteforce(text.lower(), pattern.lower())
        if position != -1:
            value = row["value"]
            if pattern not in patterns:
                patterns.append(pattern)
            if value in match:
                match_same.append(value)
            else:
                match.append(value)

    if match_same:
        print(f"[+] pattern \t: {', '.join(patterns)}")
        print(f"[*] value \t: {', '.join(match_same)}")
    else:
        print(f"[+] pattern \t: {', '.join(patterns)}")
        print(f"[*] value \t: {', '.join(match)}")

    end = time.perf_counter()  # selesai timer
    duration = end - start
    print(f"[!] waktu \t: {duration:.6f} detik\n")

if __name__ == "__main__":
    print(f"{'=' * 40} bruteforce {'=' * 40}")

    main("hewan berkaki 2")
    main("hewan berkaki 4 yang hidup di hutan")
    main("hewan berkaki 2 yang suka makan rumput")