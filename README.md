# Studi Kasus 1 — Object-Oriented Programming (Python)

Proyek ini merupakan demonstrasi konsep **Object-Oriented Programming (OOP)** dalam Python, mencakup penerapan *class*, *inheritance*, *composition*, serta *many-to-many relationships* antara objek **Student** dan **Professor**.

Struktur utama proyek terdiri dari:
- `models.py` — Implementasi seluruh kelas inti: `Address`, `Person`, `Student`, `Professor`.
- `main.py` — Skrip demonstrasi untuk menampilkan cara kerja setiap kelas melalui pemanggilan fungsi `demo()`.


🧩 Penjelasan Kode (models.py)

 1. Class Address

Merepresentasikan alamat lengkap seseorang.

Atribut:

* `street` : Jalan
* `city` : Kota
* `state` : Negara bagian/provinsi
* `postalCode` : Kode pos (integer)
* `country` : Negara

Metode Utama:

* `validate()`
  Memeriksa apakah seluruh data alamat valid, terutama kode pos harus bertipe integer dan bernilai positif.

* `outputAsLabel()`
  Mengembalikan format alamat yang tersusun seperti label pengiriman.


2. Class Person

Kelas dasar untuk *Student* dan *Professor*.

Atribut:

* `name`
* `phoneNumber`
* `emailAddress`
* `address` (objek `Address`)
* `_has_parking_pass`

Metode:

* `purchaseParkingPass()`
  Menandai bahwa orang tersebut telah membeli izin parkir.

* `hasParkingPass()`
  Mengembalikan status izin parkir.

* `set_address(address)`
  Menambahkan/mengubah alamat.

* `get_address_label()`
  Mengembalikan alamat dalam format label jika tersedia.

3. Class Student (subclass Person)

Atribut:

* `studentNumber`
* `averageMark`
* `_seminars_taken`
* `supervisors` (list of `Professor`) — relasi **many-to-many**

Metode Utama:

* `isEligibleToEnroll()`
  Menentukan apakah mahasiswa memenuhi kriteria, berdasarkan nilai rata-rata (≥60).

* `add_seminar(n)`
  Menambah jumlah seminar yang diikuti mahasiswa.

* `add_supervisor(prof)`
  Menambahkan dosen pembimbing.
  Berisi validasi:

  * Tidak boleh lebih dari 5 pembimbing
  * Relasi bersifat dua arah (menambahkan ke supervisee professor)

* `remove_supervisor(prof)`
  Menghapus pembimbing dan memperbarui hubungan dua arah.


4. **Class Professor (subclass Person)**

Atribut:

* `staffNumber`
* `salary`
* `yearsOfService`
* `numberOfClasses`
* `supervisees` — daftar mahasiswa bimbingan

Metode Utama:

* `supervise(student)`
  Menambahkan mahasiswa bimbingan melalui mekanisme dua arah di `Student`.

* `stop_supervising(student)`
  Menghapus relasi pembimbing–mahasiswa.

* `list_supervisees()`
  Menampilkan seluruh supervisee yang terdaftar.

---

 ▶️ Penjelasan Kode (main.py)

File `main.py` digunakan untuk mendemonstrasikan cara kerja semua kelas.

Berikut proses yang ditampilkan dalam fungsi `demo()`:

 1. Membuat dan memvalidasi alamat

```python
addr = Address('123 Elm St', 'Springfield', 'IL', 62704, 'USA')
addr.validate()
addr.outputAsLabel()
```

2. Membuat objek `Person` dan memberi parking pass

```python
p = Person('Alice Example')
p.purchaseParkingPass()
```

3. Membuat `Professor` dan menetapkan alamat

```python
prof = Professor('Dr. John', staffNumber=1001, salary=80000, ...)
prof.set_address(addr)
```

4. Membuat dua mahasiswa

```python
s1 = Student('Bob Student', 2001, averageMark=75)
s2 = Student('Carol Student', 2002, averageMark=58)
```

5. Menetapkan hubungan *supervisee*

Profesor menjadi pembimbing kedua student:

```python
prof.supervise(s1)
prof.supervise(s2)
```

Hasilnya:

* Profesor punya daftar supervisee
* Mahasiswa punya daftar supervisor

6. Mengecek eligibility mahasiswa

`Bob` eligible, `Carol` tidak, karena nilai < 60.

7. Mencatat seminar yang diikuti mahasiswa

```python
s1.add_seminar(2)
```

---

📂 Struktur Folder Project

```text
Tugas-1/
│── main.py
│── models.py
└── README.md
```



# Studi Kasus 2 — Library Management System (OOP Python)

Proyek ini menampilkan penerapan konsep **Object-Oriented Programming (OOP)** melalui sistem perpustakaan sederhana. Empat kelas utama digunakan untuk merepresentasikan entitas penting:
Author, LibraryItem, Book, dan LibraryMember.

Struktur file:
- `models.py` — Implementasi kelas dan relasi objek.
- `main.py` — Entry point untuk demontrasi penggunaan kelas.
  
---

## 🚀 Cara Menjalankan Program

Pastikan lingkungan Python aktif dan jalankan:

```bash
python main.py
````

Program akan menampilkan proses:

1. Membuat penulis
2. Membuat buku
3. Menampilkan informasi buku
4. Menghitung denda
5. Member meminjam dan mengembalikan buku

---

# 🧩 Penjelasan Kode (`models.py`)

## 1. **Class Author**

Merepresentasikan penulis buku.

### Atribut:

* `name` — nama penulis
* `birth_year` — tahun lahir penulis

### Metode:

* `get_age(current_year)`
  Menghitung umur penulis berdasarkan tahun saat ini.

---

## 2. **Class LibraryItem**

Kelas dasar untuk semua item perpustakaan.

### Atribut:

* `item_id` — ID unik item
* `title` — judul item

### Metode:

* `display_info()`
  Menampilkan informasi dasar item.

* `calculate_late_fee(days_late)`
  Menghitung denda keterlambatan default: **1.0 per hari**.

Kelas ini menjadi *parent class* bagi berbagai jenis item seperti buku, majalah, DVD, dll.

---

## 3. **Class Book (Subclass of LibraryItem)**

Merepresentasikan buku dan memperluas `LibraryItem`.

### Atribut tambahan:

* `isbn` — kode ISBN buku
* `author` — objek `Author` yang menulis buku tersebut

### Override:

* `display_info()`
  Menampilkan informasi spesifik buku: ISBN, judul, dan nama penulis.

* `calculate_late_fee()`
  Menggunakan tarif khusus buku: **2.0 per hari**.

---

## 4. **Class LibraryMember**

Merepresentasikan anggota perpustakaan.

### Atribut:

* `member_id`
* `name`
* `borrowed_items` — list item yang sedang dipinjam

### Metode:

* `borrow_item(item)`
  Menambah item ke daftar pinjaman, lalu menampilkan pesan konfirmasi.

* `return_item(item)`
  Menghapus item dari daftar pinjaman.
  Jika item tidak ditemukan, tampilkan peringatan.

---

▶️ Penjelasan Kode (`main.py`)

Fungsi `demo()` memperlihatkan cara penggunaan seluruh kelas.

1. Membuat penulis

```python
author = Author(name="Tere Liye", birth_year=1979)
author.get_age(2025)
```

Program menampilkan umur penulis pada tahun 2025.


2. Membuat buku

```python
book = Book(isbn="9786020324780", title="Bumi", author=author)
book.display_info()
book.calculate_late_fee(3)
```

Ditampilkan:

* Info buku
* Perhitungan denda keterlambatan 3 hari


3. Membuat anggota perpustakaan

```python
member = LibraryMember(member_id=101, name="Andi")
```

4. Member meminjam buku

```python
member.borrow_item(book)
```

Buku ditambahkan ke daftar `borrowed_items`.


5. Menampilkan daftar pinjaman

```python
for item in member.borrowed_items:
    print("-", item.title)
```


6. Mengembalikan buku

```python
member.return_item(book)
```

Item dihapus dari daftar pinjaman.



📂 Struktur Project

```text
Studi-Kasus-2/
│── main.py
│── models.py
└── README.md

Kesimpulan Studi Kasus 1

Model ini sudah mencerminkan struktur objek secara nyata dan terintegrasi,dengan pemanfaatan konsep OOP lengkap (inheritance, composition, relationship, encapsulation).
Program menunjukkan simulasi akademik yang masuk akal dan siap dikembangkan lebih lanjut.

Kesimpulan Studi Kasus 2

Sistem berhasil menerapkan konsep OOP dasar yang sangat kuat: inheritance, overriding, composition, dan list management.
Model ini mudah dikembangkan menjadi sistem perpustakaan yang lebih kompleks, seperti batas pinjaman atau tipe item lain.
