class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

        self.size += 1

    def search(self, position):
        current_element = self.head

        for _ in range(0, position):
            if current_element.next:
                current_element = current_element.next
            else:
                return "No such element!"

        return current_element.data

    def remove_at(self, remove_position):
        if remove_position >= self.size | remove_position < 0:
            print("The list does not have a element at position:", str(remove_position))

        if remove_position == 0:
            self.head = self.head.next
            self.size -= 1
            return

        current_index = 0

        current_element = self.head
        while current_element:
            if current_index == remove_position - 1:
                current_element.next = current_element.next.next
                break

            current_index += 1
            current_element = current_element.next
        self.size -= 1

    def print(self):
        print("List size:", self.size)
        current = self.head
        for current_index in range(0, self.size):
            current_element_output = current.data if current is not None else "N/A"
            next_element_output = current.next.data if current.next is not None else "N/A"
            print("Index:", current_index,
                  "\tElement:", current_element_output,
                  "\tNext:", next_element_output)
            current = current.next
