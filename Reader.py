from random import randint

from LinkedKList import KList
from LinkedList import List


def make_list_from_file(path="binfile.bin", k=1):
    l_list = KList(k) if k > 1 else List()  # chooses list implementation
    f = open(path, "rb")
    for num in list(f.read()):
        l_list.insert(num)
    f.close()
    return l_list


def create_file():
    f = open("binfile.bin", "wb")
    generated_values = []
    for _ in range(500):
        generated_values.append(randint(10, 255))
    f.write(bytearray(generated_values))
    f.close()
