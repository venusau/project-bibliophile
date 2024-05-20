class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.length=0
    def append(self, data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.length=self.length+1
        else:
            current=self.head
            while not current.next==None:
                current=current.next
            current.next=new_node
            self.length=self.length+1
    def insert_at_position(self, data, position):
        if position <= 0:
            print("Invalid position. Position should be a positive integer.")
            return

        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
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
        current.next = new_node
    def display(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            current=self.head
            while current:
                print(current.data,end="->")
                current=current.next
                

    def display_middle(self):
        if self.head==None:
            print("Linked list is empty")
        
        elif self.length<3:
            print("Not enough elements to display the middle element !")

        else:
            c=self.length
            if c %2==0:
                c=c//2
                current=self.head
                while current.next and not c==0 :
                    current=current.next
                    c=c-1
                
                print(current.next.data)

            else:
                c=c//2
                current=self.head
                while current.next and not c==0 :
                    current=current.next
                    c=c-1
                print(current.data)
                

linked_list = SinglyLinkedList()

print("Press 1 to append a word, 2 to insert at a position,3 for displaying the middle, or 0 to end:")
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
    elif n==3:
        linked_list.display_middle()
    else:
        print("Invalid choice.")

    linked_list.display()

    print("Press 1 to append a word, 2 to insert at a position, or 0 to end:")
    n = int(input())


