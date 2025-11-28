"""
models.py
Implementasi Studi Kasus 2:
Author, Book, LibraryItem, LibraryMember
"""

from typing import List, Optional


class Author:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    def get_age(self, current_year: int) -> int:
        """Hitung umur berdasarkan tahun sekarang."""
        return current_year - self.birth_year


class LibraryItem:
    def __init__(self, item_id: int, title: str):
        self.item_id = item_id
        self.title = title

    def display_info(self):
        """Tampilkan informasi item."""
        print(f"Item ID: {self.item_id}")
        print(f"Title: {self.title}")

    def calculate_late_fee(self, days_late: int) -> float:
        """Default late fee = 1.0 per hari."""
        return days_late * 1.0


class Book(LibraryItem):
    def __init__(self, isbn: str, title: str, author: Author):
        super().__init__(item_id=0, title=title)
        self.isbn = isbn
        self.author = author

    def display_info(self):
        """Menampilkan info book."""
        print(f"ISBN: {self.isbn}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author.name}")

    def calculate_late_fee(self, days_late: int) -> float:
        """Buku menggunakan biaya keterlambatan khusus: 2.0 per hari."""
        return days_late * 2.0


class LibraryMember:
    def __init__(self, member_id: int, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_items: List[LibraryItem] = []

    def borrow_item(self, item: LibraryItem):
        """Pinjam 1 item."""
        self.borrowed_items.append(item)
        print(f"{self.name} borrowed '{item.title}'.")

    def return_item(self, item: LibraryItem):
        """Kembalikan item."""
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            print(f"{self.name} returned '{item.title}'.")
        else:
            print("Item not found in borrowed list.")