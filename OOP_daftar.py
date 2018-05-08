class Daftar():
    def __init__(self, alamat="", telpon=""):
        self.nama=[]
        self.alamat=alamat
        self.telpon=telpon
    def __str__(self):
        return "Nama pelanggan adalah {} ".format(self.nama)
    def tambahNama(self,nama):
        self.nama.append(nama)
        return "{} berhasil ditambahkan".format(self.nama)
    def __len__(self):
        return len(self.nama)


data=Daftar()
print(data.tambahNama("budi"))
print(len(data))
print(data.tambahNama("tono"))
print(len(data))
