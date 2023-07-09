# mengubah type data list menjadi tipe data set
list = ["aria", "fatah"]
list_to_set_= set(list)

install = {"chrome", "facebook", "visual studio"}
prefered = {"browsser", "chrome", "firefox"}

# union = menggabungkan key
print(".union():" ,install.union(prefered))

# intersection = mencari persamaan key
print(".intersection():" ,install.intersection(prefered))

# difference = mencari perbedaan key
print(".difference():" ,install.difference(prefered))