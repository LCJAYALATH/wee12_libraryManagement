class BookNode:
    """Represents a single node in Team 2's Binary Search Tree."""
    def __init__(self, title: str, book_id: str):
        self.search_key = title.lower()  # Normalized key for alphabetical sorting
        self.book_id = book_id           # Shared contract key used across all modules
        self.left = None                 # Left child pointer
        self.right = None                # Right child pointer


class SearchEngine:
    """Handles BST indexing and lookups for the Shared Catalog."""
    def __init__(self):
        self.root = None

    def add_book(self, title: str, book_id: str):
        """Public method to insert a new book into the search index."""
        self.root = self._insert(self.root, title, book_id)

    def _insert(self, node, title: str, book_id: str) -> BookNode:
        """Helper method to recursively insert a node into the BST."""
        if node is None:
            return BookNode(title, book_id)
        
        normalized_title = title.lower()
        if normalized_title < node.search_key:
            node.left = self._insert(node.left, title, book_id)
        else:
            node.right = self._insert(node.right, title, book_id)
            
        return node

    def find_book_id(self, title: str) -> str:
        """Public search method. Returns the shared book_id string or None."""
        result_node = self._search(self.root, title.lower())
        return result_node.book_id if result_node else None

    def _search(self, node, target_key: str) -> BookNode:
        """Helper method to recursively traverse the tree looking for the key."""
        if node is None or node.search_key == target_key:
            return node
        
        if target_key < node.search_key:
            return self._search(node.left, target_key)
        return self._search(node.right, target_key)