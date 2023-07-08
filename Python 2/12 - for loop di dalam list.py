# data asli
id = ["X12", "M45", "Z10"]

# id_1
id_1 = ["0. " + value for value in id] #jadi kesimpulanya variable value adalah for value in id
print(id_1)

# id 2
id_2 = []
for value in id:
    new_value = "1. " + value
    id_2.append(new_value)

print(id_2)

# contoh lain
boolean = [True, False, True]

data_diubah = {not bool for bool in boolean}
print(data_diubah)
# jadi True False True akan diubah menjadi sebaliknya dan
# bool for bool in boolran akan meloop sebanyak data boolean
# yaitu 3x namun yang akan masuk kedalam set/dictionary hanya
# 1 per key alias ga bisa double 

# contoh kedua
bundle = ["vanila", "cokelat"]

ice_cream_1 = []
for item in bundle:
    update = item.replace("matcha", "stroberi")
    ice_cream_1.append(update)
print(ice_cream_1)

ice_cream_2 = [item.replace("matcha", "stroberi") for item in bundle]
print(ice_cream_2)

# contoh ketiga
ratings = [4.3, 3.1, 5, 1.1]

recommended = [rating > 4 for rating in ratings]
print(recommended)