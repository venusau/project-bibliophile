import tkinter as tk
from tkinter import simpledialog, messagebox

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

    # Other methods like insert_at_position go here...

class CircularDoublyLinkedListGUI:
    def __init__(self):
        self.linked_list = CircularDoublyLinkedList()

        self.root = tk.Tk()
        self.root.title("Circular Doubly Linked List GUI")

        self.label = tk.Label(self.root, text="Circular Doubly Linked List")
        self.label.pack()

        self.append_button = tk.Button(self.root, text="Append", command=self.append_dialog)
        self.append_button.pack()

        self.insert_button = tk.Button(self.root, text="Insert at Position", command=self.insert_dialog)
        self.insert_button.pack()

        self.display_button = tk.Button(self.root, text="Display", command=self.display)
        self.display_button.pack()

    def append_dialog(self):
        word = simpledialog.askstring("Append", "Enter the word to be appended:")
        if word:
            self.linked_list.append(word)
            messagebox.showinfo("Success", f"'{word}' appended to the list.")

    def insert_dialog(self):
        word = simpledialog.askstring("Insert", "Enter the word to be inserted:")
        if word:
            position_str = simpledialog.askstring("Insert", "Enter the position where you want to insert the word:")
            try:
                position = int(position_str)
                self.linked_list.insert_at_position(word, position)
                messagebox.showinfo("Success", f"'{word}' inserted at position {position}.")
            except ValueError:
                messagebox.showerror("Error", "Invalid position. Please enter a valid position (a positive integer).")

    def display(self):
        if not self.linked_list.head:
            messagebox.showinfo("Info", "The list is empty.")
        else:
            content = "Circular Doubly Linked List: "
            current = self.linked_list.head
            while True:
                content += str(current.data) + " <-> "
                current = current.next
                if current == self.linked_list.head:
                    break
            content = content[:-5]  # Remove the last " <-> " for circular visualization
            content += " <-> ... "  # Indicate the circular part
            messagebox.showinfo("List Content", content)

    def run(self):
        self.root.mainloop()

# Example usage:
gui = CircularDoublyLinkedListGUI()
gui.run()
