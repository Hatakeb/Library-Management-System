from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Staff, Liberian

class StudentUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(StudentUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']

class LiberianStudentStatusForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Status']

class StaffDetailsForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ['user']

class LiberianStaffStatusForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['Status']

class StaffUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(StaffUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class StaffDetailsForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ['user']

class LiberianUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(LiberianUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LiberianDetailsForm(forms.ModelForm):
    class Meta:
        model = Liberian
        exclude = ['user']

from django import forms
from .models import Book, Author, Category

class BookForm(forms.ModelForm):
    authors = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter authors, separated by commas. Each author as Firstname Lastname'}),
        help_text='Enter multiple authors separated by commas. Example: John Doe, Jane Smith'
    )
    categories = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter categories, separated by commas.'}),
        help_text='Enter multiple categories separated by commas. Example: Fiction, Science, History'
    )

    class Meta:
        model = Book
        fields = ['BookID', 'Title', 'DatePublished', 'CopiesOwned']

    def save(self, commit=True):
        book = super().save(commit=False)
        if commit:
            book.save()
        # Process authors field
        authors_str = self.cleaned_data.get('authors', '')
        author_names = [a.strip() for a in authors_str.split(',') if a.strip()]
        book.Authors.clear()
        for name in author_names:
            parts = name.split()
            if len(parts) >= 2:
                first_name = parts[0]
                last_name = ' '.join(parts[1:])
            elif len(parts) == 1:
                first_name = parts[0]
                last_name = ''
            else:
                continue
            author, created = Author.objects.get_or_create(FirstName=first_name, LastName=last_name)
            book.Authors.add(author)
        # Process categories field
        categories_str = self.cleaned_data.get('categories', '')
        category_names = [c.strip() for c in categories_str.split(',') if c.strip()]
        book.Categories.clear()
        for cname in category_names:
            category, created = Category.objects.get_or_create(name=cname)
            book.Categories.add(category)
        return book
