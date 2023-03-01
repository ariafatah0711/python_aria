# date time
import datetime

data_waktu = datetime.datetime.now()
print(f"datetime.now(): {data_waktu}")
print(f"data_waktu.year: {data_waktu.year}")
print(f"data_waktu.strftime('%A'): {data_waktu.strftime('%A')}")

# collections
from collections import Counter

data = ["a", "b", "a", "c", "e", "a", "b", "d", "c"]
data_count = Counter(data)
print(f"data count: {data_count}")
print(f"jumlah a: {data_count['a']}")
# count = 0
# for i in data:
#     if i == "a":
#         count += 1
# print(count)

# import file
import io

# file = io.open("file_text.txt","r")
# print(file.read()) # gajelas ga keluar wkwkwk # ternyata harus file yang ada di dalam folder pertama