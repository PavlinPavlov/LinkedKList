from LinkedKList import KList, KNode

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

    print("Debug - search before removal:", ll.search(11))
    ll.print()
    ll.remove_at(4)
    ll.remove_at(4)
    ll.remove_at(3)
    print("Debug - search after removal:", ll.search(11))
    ll.print()
