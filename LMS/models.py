from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    BookID= models.AutoField(primary_key=True)
    Title= models.CharField(max_length=100)
    Categories= models.ManyToManyField('Category')
    Author= models.CharField(max_length=100)
    Authors= models.ManyToManyField('Author')
    DatePublished=models.DateField()
    CopiesOwned= models.IntegerField()

    def __str__(self):
        return self.Title

class Author(models.Model):
    AuthorID= models.AutoField(primary_key= True)
    FirstName= models.CharField(max_length=100)
    LastName= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Student(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Suspended', 'Suspended'),
        ('Not Active', 'Not Active'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    MatriculationNumber= models.CharField(max_length=100)
    FirstName= models.CharField(max_length=100)
    MiddleName= models.CharField(max_length=100)
    LastName= models.CharField(max_length=100)
    DateJoined= models.DateField(auto_now_add=True)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.MatriculationNumber

class Staff(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Suspended', 'Suspended'),
        ('Not Active', 'Not Active'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    StaffID= models.CharField(max_length=100)
    FirstName= models.CharField(max_length=100)
    MiddleName= models.CharField(max_length=100)
    LastName= models.CharField(max_length=100)
    DateJoined= models.DateField(auto_now_add=True)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.StaffID

class Liberian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    LiberianID= models.CharField(max_length=100)
    FirstName= models.CharField(max_length=100)
    MiddleName= models.CharField(max_length=100)
    LastName= models.CharField(max_length=100)

    def __str__(self):
        return self.LiberianID

class Borrowed(models.Model):
    BorrowID= models.AutoField(primary_key=True)
    BookID= models.ForeignKey('Book', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', null=True, blank=True, on_delete=models.CASCADE)
    staff = models.ForeignKey('Staff', null=True, blank=True, on_delete=models.CASCADE)
    BorrowedDate= models.DateField(auto_now_add=True)
