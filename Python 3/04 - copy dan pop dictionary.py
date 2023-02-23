# copy dictionary

teman_teman = {
    "cup":"ucup ganteng",
    "tong":"otong gentong",
    "dung":"udung bau udang",
    "sep":"asep si paling asik",
    "cuy":"ucup si paling cuy"
}

print("belum tercopy / friend ikut berubah")
# belum di copy

friend = teman_teman
teman_teman["cup"] = "ucup jelek"

print(f"teman-teman: {teman_teman}\n")
print(f"friend: {friend}\n")
teman_teman["cup"] = "ucup ganteng"

print("sudah tercopy friend tidak berubah")
# .copy()

friend = teman_teman.copy()
teman_teman["cup"] = "ucup jelek"

print(f"teman-teman: {teman_teman}\n")
print(f"friend: {friend}\n")

# pop dictioonary
# pop itu mentransfer data friend pop di transfeer ke data_asep
data_asep =friend.pop("sep")
print(f"data asep: {data_asep}")
print("friend:", friend)

# pop item dictionary
# mengambil pasangan yang terakhir
data_terakhir = friend.popitem()
print(f"\ndata terakhir: {data_terakhir}")
print("friend:", friend)