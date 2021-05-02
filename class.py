class class_saya:
    def __init__(self, name, age):
        self.nama = name
        self.umur = age
    def salam(self):
        print(f"My name is {self.nama}")
    def leaving(self):
        print(f"Good bye!")
orang1 = class_saya("Tyo","19")
orang2 = class_saya("Jony","23")

print(orang1.nama)
print(orang2.nama)
print( )
print(orang1.umur)
print(orang2.umur)
orang1.salam()
orang1.leaving()