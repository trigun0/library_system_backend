from django.db import models

# 1️⃣ Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name


# 2️⃣ Genre Model
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# 3️⃣ Book Model (ForeignKeys → Author, Genre)
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="books")
    published_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} ({self.author.name})"


# 4️⃣ Borrow Model (ForeignKey → Book)
class Borrow(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="borrow_records")
    borrower_name = models.CharField(max_length=100)
    borrowed_on = models.DateField()  # ✅ changed from auto_add so frontend can choose
    return_date = models.DateField(blank=True, null=True)  # ✅ added new field
    rented_days = models.PositiveIntegerField()
    charges = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.borrower_name} borrowed {self.book.title}"