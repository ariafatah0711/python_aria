# teknik menduplikat list

a = ["ucup", "dudung", "otong", "aria"]
print(f"\na: {a}")

b = a
print(f"b: {b}")

# ubah member a

# ini akan merubah kedua list
a[1] = "micheal"
b.sort
print(f"\na: {a}")
print(f"b: {b}")

# addres dari kedua list a dan b
print(f"addres a: {hex(id(a))}")
print(f"addres b: {hex(id(b))}")

# menduplikat data

print("\nmembuat list c dengan a.copy")
c = a.copy() # membuata data baru / full duplikat

print(f"addres a: {hex(id(a))}")
print(f"addres b: {hex(id(b))}")
print(f"addres c: {hex(id(c))}")

print(f"\na: {a}")
print(f"b: {b}")
print(f"c: {c}")

print("\nkita ubah data micheal menjadi dadang")
c[1] = "dadang"

print(f"\na: {a}")
print(f"b: {b}")
print(f"c: {c}")