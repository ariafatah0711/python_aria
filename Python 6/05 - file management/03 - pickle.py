# Pickle => Object Serialization pada Python. 
    # Pickling adalah istilah untuk mengubah objek menjadi byte stream, 
    # sedangkan unpickling adalah perlakuan sebaliknya.

# import pickle
# contoh_dictionary = {1:"6", 2:"2", 3:"f"}
# pickle_keluar = open("dict.pickle","wb")
# pickle.dump(contoh_dictionary, pickle_keluar)
# pickle_keluar.close()

import pickle
pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()
 
print(contohDictionary)