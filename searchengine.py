# ---------- Book Class ----------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
# ==========================================
# Binary Search Tree (BST)
# ==========================================
class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Insert a book into BST
    def insert(self, book):
        self.root = self._insert(self.root, book)

    def _insert(self, node, book):

        if node is None:
            return BSTNode(book)

        if book.title.lower() < node.book.title.lower():
            node.left = self._insert(node.left, book)

        else:
            node.right = self._insert(node.right, book)

        return node

    # Recursive search by title
    def search_by_title(self, title):
        return self._search(self.root, title)

    def _search(self, node, title):

        if node is None:
            return None

        if title.lower() == node.book.title.lower():
            return node.book

        elif title.lower() < node.book.title.lower():
            return self._search(node.left, title)

        else:
            return self._search(node.right, title)

# ==========================================
# Linked List
# ==========================================

class AuthorNode:

    def __init__(self, book):
        self.book = book
        self.next = None

class AuthorLinkedList:

    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, book):

        new_node = AuthorNode(book)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # Search by author
    def search_by_author(self, author):

        current = self.head
        found = False

        while current:

            if current.book.author.lower() == author.lower():
                print("--------------------------------")
                print("Title :", current.book.title)
                print("Author:", current.book.author)
                found = True

            current = current.next

        if not found:
            print("No books found for this author.")


# ==========================================
# Sample Library Data
# ==========================================

books = [

    Book("Python Basics", "John"),

    Book("Algorithms", "Bob"),

    Book("Database Systems", "Alice"),

    Book("Machine Learning", "David"),

    Book("Data Structures", "Alice"),

    Book("Computer Networks", "James"),

    Book("Artificial Intelligence", "David"),

    Book("Operating Systems", "Bob")

]

# Create BST and Linked List
catalog_tree = BinarySearchTree()
author_list = AuthorLinkedList()

# Insert books into both structures
for book in books:
    catalog_tree.insert(book)
    author_list.insert(book)


# ==========================================
# Main Menu
# ==========================================

while True:

    print("\n========== Library Search Engine ==========")
    print("1. Search Book by Title (BST)")
    print("2. Search Books by Author (Linked List)")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        title = input("Enter Book Title: ")

        result = catalog_tree.search_by_title(title)

        if result:
            print("\nBook Found")
            print("----------------------------")
            print("Title :", result.title)
            print("Author:", result.author)
        else:
            print("\nBook Not Found.")

    elif choice == "2":

        author = input("Enter Author Name: ")

        print("\nBooks by", author)
        author_list.search_by_author(author)

    elif choice == "3":

        print("Thank you!")
        break

    else:

        print("Invalid choice.")