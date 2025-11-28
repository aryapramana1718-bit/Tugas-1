"""
main.py
Entry point Studi Kasus 2
Run: python main.py
"""

from models import Author, Book, LibraryItem, LibraryMember


def demo():

    # 1. Buat Author
    author = Author(name="Tere Liye", birth_year=1979)
    print("Author Age (2025):", author.get_age(2025))

    print("\n---\n")

    # 2. Buat Book
    book = Book(isbn="9786020324780", title="Bumi", author=author)
    book.display_info()
    print("Late Fee (3 days):", book.calculate_late_fee(3))

    print("\n---\n")

    # 3. Buat Member
    member = LibraryMember(member_id=101, name="Andi")

    # Pinjam buku
    member.borrow_item(book)

    # Cek daftar pinjaman
    print("\nBorrowed Items:")
    for item in member.borrowed_items:
        print("-", item.title)

    print("\n---\n")

    # Kembalikan buku
    member.return_item(book)


if __name__ == "__main__":
    demo()