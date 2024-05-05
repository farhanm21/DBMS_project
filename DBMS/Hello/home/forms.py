from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from .models import Book, Author
# from .models import Student
# from django.contrib.auth.forms import AuthenticationForm  # Add this import
# from .models import StudentUser

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)

# class BookForm(forms.ModelForm):
# 	class Meta:
# 		model = Book
# 		fields = ['title', 'author', 'isbn', 'genre']
# 		widgets = {
# 				'title': forms.TextInput(attrs={'class': 'form-control'}),
# 				'author': forms.TextInput(attrs={'class': 'form-control'}),
# 				'isbn': forms.TextInput(attrs={'class': 'form-control'}),
# 				'genre': forms.TextInput(attrs={'class': 'form-control'}),
# 			}

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
	class Meta:
			model = Book
			fields = ['title', 'author', 'isbn', 'genre']
			widgets = {
				'title': forms.TextInput(attrs={'class': 'form-control'}),
				'author': forms.TextInput(attrs={'class': 'form-control'}),
				'isbn': forms.TextInput(attrs={'class': 'form-control'}),
				'genre': forms.Select(attrs={'class': 'form-control'}),
			}


class SearchForm(forms.Form):
    isbn = forms.CharField(max_length=20, label='Enter ISBN Number')


# class StudentRegistrationForm(UserCreationForm):
#     email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
#     first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
#     last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
#     student_id = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Student ID'}))
#     phone_number = forms.CharField(label="", max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
#     address = forms.CharField(label="", max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))
#     date_of_birth = forms.DateField(label="", widget=forms.DateInput(attrs={'type':'date', 'class':'form-control', 'placeholder':'Date of Birth'}))
#     password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
#     password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super(StudentRegistrationForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['username'].widget.attrs['placeholder'] = 'Username'
#         self.fields['username'].label = ''
#         self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['placeholder'] = 'Password'
#         self.fields['password1'].label = ''
#         self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

#         self.fields['password2'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
#         self.fields['password2'].label = ''
#         self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

# class StudentLoginForm(AuthenticationForm):
#     # You can customize this form if needed, e.g., to use email as the login field
#     class Meta:
#         fields = ['username', 'password']


# class StudentUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = StudentUser
#         fields = ('username', 'email', 'first_name', 'last_name', 'student_id', 'phone_number', 'address', 'date_of_birth')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)