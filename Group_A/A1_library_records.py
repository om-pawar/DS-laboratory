# Experiment A1: Library Book Borrowing Records
# Group A: Arrays and Searching Sorting Algorithms

def analyze_library_records(member_borrows, book_counts):
    # 1. Compute average number of books borrowed by all members
    avg_borrows = sum(member_borrows) / len(member_borrows) if member_borrows else 0
    
    # 2. Find book with highest and lowest number of borrowings
    max_book = max(book_counts, key=book_counts.get)
    min_book = min(book_counts, key=book_counts.get)
    
    # 3. Count members who have borrowed 0 books
    zero_count = sum(1 for x in member_borrows if x == 0)
    
    # 4. Display most frequently borrowed book (mode of borrow counts)
    freq = {}
    for count in book_counts.values():
        freq[count] = freq.get(count, 0) + 1
    mode_count = max(freq, key=freq.get)
    most_freq_books = [k for k, v in book_counts.items() if v == mode_count]

    print("--- Library Borrowing Analysis ---")
    print(f"1. Average books borrowed per member : {avg_borrows:.2f}")
    print(f"2. Highest borrowed book             : {max_book} ({book_counts[max_book]} times)")
    print(f"   Lowest borrowed book              : {min_book} ({book_counts[min_book]} times)")
    print(f"3. Members with 0 borrowings         : {zero_count}")
    print(f"4. Mode of borrow counts             : {mode_count} (Books: {most_freq_books})")


if __name__ == "__main__":
    members_data = [3, 0, 5, 2, 0, 4, 3, 3]
    books_data = {"DSA": 12, "OS": 5, "DBMS": 12, "CN": 2, "AI": 8}
    analyze_library_records(members_data, books_data)
