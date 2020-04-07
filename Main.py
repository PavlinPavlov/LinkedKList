from asyncio import sleep

from LinkedKList import KList, KNode
from LinkedList import List
from FileUtils import create_file, make_list_from_file
import datetime

if __name__ == '__main__':
    k_list = make_list_from_file("binfile_5_000_000.bin", 1000)
    l_list = make_list_from_file("binfile_5_000_000.bin")

    print(datetime.datetime.now())
    print(l_list.search(4_670_045))
    print(datetime.datetime.now())

    print(datetime.datetime.now())
    print(k_list.search(4_670_045))
    print(datetime.datetime.now())
