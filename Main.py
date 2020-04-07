from LinkedKList import KList, KNode
from Reader import create_file, make_list_from_file

if __name__ == '__main__':
    ll = KList(3)
    ll.insert(100)
    ll.insert(11)
    ll.insert(22)
    ll.insert(33)
    ll.insert(44)
    ll.insert(55)
    ll.insert(66)
    ll.insert(77)
    ll.insert(88)
    ll.insert(99)
    ll.insert(1010)
    ll.insert(1111)

    k_list = make_list_from_file("binfile.bin", 5)
    k_list.print()
