class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            last_node = self.head.prev
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if not self.head:
            print("Empty list.")
            return

        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("")

    def insert_at_position(self, data, position):
        if position <= 0:
            print("Invalid position. Position should be a positive integer.")
            return

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            return

        current = self.head
        count = 1

        while count < position - 1:
            current = current.next
            count += 1

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node

# Example usage:
linked_list = CircularDoublyLinkedList()

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
