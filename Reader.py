from random import randint

from LinkedKList import KList


def make_list_from_file(path="binfile.bin", k=10):
    k_list = KList(k)
    f = open(path, "rb")
    for num in list(f.read()):
        k_list.insert(num)
    f.close()
    return k_list


def create_file():
    f = open("binfile.bin", "wb")
    generated_values = []
    for _ in range(500):
        generated_values.append(randint(10, 255))
    f.write(bytearray(generated_values))
    f.close()
