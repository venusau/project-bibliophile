class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def insert_at_position(self, data, position):
        if position <= 0:
            print("Invalid position. Position should be a positive integer.")
            return

        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        count = 1

        while current and count < position - 1:
            current = current.next
            count += 1

        if not current:
            print("Invalid position. The linked list is not long enough.")
            return

        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

# Example usage:
linked_list = DoublyLinkedList()

print("Press 1 to append a word, 2 to insert at a position, or 0 to end:")
n = int(input())

while n != 0:
    if n == 1:
        word = input("Enter the word to be appended: ")
        linked_list.append(word)
    elif n == 2:
        word = input("Enter the word to be inserted: ")
        position_str = input("Enter the position where you want to insert the word: ")

        try:
            position = int(position_str)
            linked_list.insert_at_position(word, position)
        except ValueError:
            print("Invalid input. Please enter a valid position (a positive integer).")

    else:
        print("Invalid choice.")

    linked_list.display()

    print("Press 1 to append a word, 2 to insert at a position, or 0 to end:")
    n = int(input())
