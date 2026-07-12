from team2_search.search_engine import SearchEngine

# Initialize Team 2's engine
engine = SearchEngine()

# Populate with mock data from the Shared Catalog
engine.add_book("The Great Gatsby", "BK-101")
engine.add_book("1984", "BK-205")
engine.add_book("To Kill a Mockingbird", "BK-309")

# Test a search lookup
query = "1984"
found_id = engine.find_book_id(query)

if found_id:
    print(f"Success! Found '{query}'. Shared book_id: {found_id}")
    print("Ready to hand this book_id over to Team 1 (Borrow) or Team 3 (Waitlist).")
else:
    print(f"Book '{query}' not found in the catalog.")