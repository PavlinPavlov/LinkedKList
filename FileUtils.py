from random import randint

from LinkedKList import KList
from LinkedList import List


def make_list_from_file(path="binfile.bin", k=1):
    file_d = open(path, "rb")
    file_content_list = list(file_d.read())

    l_list = KList(k, file_content_list) if k > 1 else List(file_content_list)

    file_d.close()
    return l_list


def create_file(nums=50_000, path="binfile.bin"):
    partition_size = 1000
    partitions = int(nums / partition_size)

    file_d = open(path, "wb")

    for a in range(partitions):
        generated_values = []
        for b in range(partition_size):
            generated_values.append(randint(10, 255))
        file_d.write(bytearray(generated_values))

    file_d.close()
