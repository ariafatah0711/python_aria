class ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def check_id(self):
        print(f"nama: {self.nama} \nmotor: {self.transmisi} \ndaerah: {self.daerah} \nid ojek: 32793794\n")

class gojek(ojek):
    # ini namanya dry mengulangi hal yang sama lebih baik tidak perlu
    # cukup tambahkan ojek di dalam parameter gojek

    def check_id(self):
        print(f"nama: {self.nama} \nmotor: {self.transmisi} \ndaerah: {self.daerah} \nid gojek: 42294394\n")


    # def __init__(self, nama, transmisi, daerah):
    #     self.nama = nama
    #     self.transmisi = transmisi
    #     self.daerah = daerah

    # def check_id(self):
    #     print(f"nama: {self.nama} \nmotor: {self.transmisi} \ndaerah: {self.daerah}")

ojek1 = ojek("maria", "manual", "bandung")
gojek2 = gojek("angga", "automatic", "bogor")

ojek1.check_id()
gojek2.check_id()

