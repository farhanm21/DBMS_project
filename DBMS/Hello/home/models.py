from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
        
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
	

    def __str__(self):
        return self.name

class Book(models.Model):
    FICTION = 'Fiction'
    NONFICTION = 'Non-Fiction'
    MYSTERY = 'Mystery'
    SCIENCE_FICTION = 'Science Fiction'
    ROMANCE = 'Romance'
    HORROR = 'Horror'
    GENRE_CHOICES = [
        (FICTION, 'Fiction'),
        (NONFICTION, 'Non-Fiction'),
        (MYSTERY, 'Mystery'),
        (SCIENCE_FICTION, 'Science Fiction'),
        (ROMANCE, 'Romance'),
        (HORROR, 'Horror'),
        # Add more choices as needed
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)

class sStudent(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)

    class Meta:
        db_table = 'student'
        managed = False


class IssueBook(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)


