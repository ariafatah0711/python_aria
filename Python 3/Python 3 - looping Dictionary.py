# looping dictionary

teman_teman = {
    "cup":"ucup ganteng",
    "tong":"otong gentong",
    "dung":"udung bau udang",
    "sep":"asep si paling asik",
    "cuy":"ucup si paling cuy"
}

# looping first try
# yang keluar adalah keynya
for teman in teman_teman:
    print(teman)

print("\n.key")
# opertaor untuk mengambil item / iterables
# mengambil key
keys = teman_teman.keys()
print(keys)

print("\nvalue")
# mengambil value
for key in teman_teman.keys():
    print(teman_teman.get(key))

print("\n.values")
# atau 
values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

print("\n.items")
items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

print("\nkey value")
# key,value

for key,value in teman_teman.items():
    print(f"key: {key}\t value: {value}")

# kesimpulan
# .keys untuk key
# .value untuk value
# .items untuk key dan value