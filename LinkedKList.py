class KNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.next_kth = None


class KList:

    def __init__(self, k=10, input_list=None):
        self.k = k
        self.size = 0
        self.head = None
        self.first_free_kth_element = self.head
        if input_list is not None:
            self.__create(input_list)

    def __create(self, input_list):
        previous_element = None
        self.first_free_kth_element = None
        for i in range(len(input_list)):
            new_node = KNode(input_list[i])
            if self.head:
                current_element = new_node
                previous_element.next = current_element
                previous_element = current_element
            else:
                self.head = new_node
                previous_element = self.head

            self.size += 1

            if self.size > self.k:  # skipping creating k links until we have k + 1 elements in the list
                if self.first_free_kth_element is None:
                    self.first_free_kth_element = self.head
                self.first_free_kth_element.next_kth = new_node
                self.first_free_kth_element = self.first_free_kth_element.next

    def insert(self, data):
        new_node = KNode(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

        self.size += 1

        if self.size > self.k:  # skipping creating k links until we have k + 1 elements in the list
            if self.first_free_kth_element is None:
                self.first_free_kth_element = self.head
            self.first_free_kth_element.next_kth = new_node
            self.first_free_kth_element = self.first_free_kth_element.next

    def search(self, position):
        normal_search_count = position % self.k
        k_search_count = position // self.k  # integer division
        print("Info - K-th searches:", k_search_count)
        print("Info - Normal searches:", normal_search_count)

        current_element = self.head

        for current_index in range(0, k_search_count):  # current_index is not used
            if current_element.next_kth:
                current_element = current_element.next_kth
            else:
                return "No such element!"

        for current_index in range(0, normal_search_count):  # current_index is not used
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
        first_alter_index = remove_position - self.k
        last_alter_index = remove_position - 1

        current_element = self.head
        while current_element:
            if (current_index >= first_alter_index) & (current_index < last_alter_index):
                if current_element.next_kth is not None:
                    current_element.next_kth = current_element.next_kth.next

            if current_index == last_alter_index:
                if current_element.next_kth is not None:
                    current_element.next_kth = current_element.next_kth.next
                current_element.next = current_element.next.next
                self.size -= 1
                break

            current_index += 1
            current_element = current_element.next

    def print_m(self, print_count=-1):
        print("List size:", self.size)
        current = self.head
        for current_index in range(0, self.size):
            if print_count == 0:
                break
            print_count -= 1
            current_element_output = current.data if current is not None else "N/A"
            next_element_output = current.next.data if current.next is not None else "N/A"
            kth_element_output = current.next_kth.data if current.next_kth is not None else "N/A"
            print("Index:", current_index,
                  "\tElement:", current_element_output,
                  "\tNext:", next_element_output,
                  "\tK-th", kth_element_output)
            current = current.next
