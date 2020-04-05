class KNode:

    def __init__(self, data, next_element=None):
        self.data = data
        self.next_element = next_element
        self.next_kth_element = None


class KList:

    def __init__(self, k=10):
        self.k = k
        self.size = 0
        self.head = None
        self.first_free_kth_element = self.head

    def insert_at_end(self, data):
        new_node = KNode(data)
        if self.head:
            current = self.head
            while current.next_element:
                current = current.next_element
            current.next_element = new_node
        else:
            self.head = new_node

        self.size += 1

        if self.size > self.k:
            if self.first_free_kth_element is None:
                self.first_free_kth_element = self.head
            self.first_free_kth_element.next_kth_element = new_node
            self.first_free_kth_element = self.first_free_kth_element.next_element

    def search(self, position):
        current_element = self.head
        for current_index in range(0, position):
            if current_element.next_element:
                current_element = current_element.next_element
            else:
                return "No such element!"
        # return current_element.data
        return current_element

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next_element
