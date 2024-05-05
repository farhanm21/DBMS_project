

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from .forms import BookForm
from .models import Book
# from .forms import StudentRegistrationForm
# from .forms import StudentLoginForm
from .forms import SearchForm
from django.db import connection
from django.http import HttpResponse


def user_login(request):
	records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('loginn')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('loginn')
	else:
		return render(request, 'loginn.html', {'records':records})



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('loginn')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('loginn')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginn')  # Redirect to a URL name for book list page
    else:
        form = BookForm()
    return render(request, 'addbook.html', {'form': form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('loginn')



def starter(request):
    return render(request, 'starter.html')


def all_books(request):
    if request.user.is_authenticated:
        all_books = Book.objects.all()
        return render(request, 'ava_books.html', {'ava_books': all_books})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('loginn')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('loginn')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('loginn')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('loginn')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('loginn')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('loginn')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('loginn')


def search_books(request):
    book_details = None
    book_not_found = False  # Initialize a variable to track if the book is not found
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            # Retrieve the book details based on the ISBN number
            try:
                book_details = Book.objects.get(isbn=isbn)
            except Book.DoesNotExist:
                book_not_found = True  # Set the variable to True if book is not found
    else:
        form = SearchForm()
    return render(request, 'search_books.html', {'form': form, 'book_details': book_details, 'book_not_found': book_not_found})



def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_login')  # Redirect to the student dashboard after login
    else:
        form = StudentLoginForm()
    return render(request, 'student_login.html', {'form': form})


def student_reg(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')  # Assuming you have a named URL pattern for login
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_reg.html', {'form': form})

def Stud_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM student WHERE username = %s AND password = %s", [username, password])
            row = cursor.fetchone()

            if row:
                # Authentication successful
                # Perform any additional actions, such as setting session variables
                return redirect('display_table')
            else:
                # Authentication failed
                return render(request, 'student_login.html', {'error_message': 'Invalid username or password.'})
    else:
        # If it's not a POST request, render the login page
        return render(request, 'student_login.html')



from .models import Book  # Import the Book model

def display_table(request):
    # Fetch all rows from home_book table
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM home_book")
        rows = cursor.fetchall()  # Fetch all rows from the result

    # Fetch available books using the Book model
    available_books = Book.objects.all()

    # Pass the fetched data to the template
    return render(request, 'display_table.html', {'rows': rows, 'available_books': available_books})



def register_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        with connection.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO student (username, password, email) VALUES (%s, %s, %s)", [username, password, email])
            except Exception as e:
                error_message = str(e)
                return render(request, 'new_reg.html', {'error_message': error_message})
        
        return redirect('student_login')  # Redirect to student_login page upon successful registration
    else:
        return render(request, 'new_reg.html') 




def issued_books(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT b.title, b.author, b.isbn, b.genre, s.username AS student_name
            FROM issued_book ib
            JOIN home_book b ON ib.book_id = b.id
            JOIN student s ON ib.student_id = s.id
        """)
        books_with_students = cursor.fetchall()
    return render(request, 'issued_books.html', {'books_with_students': books_with_students})

from datetime import date

def issue_book(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        book_id = request.POST.get('book_id')
        
        try:
            # Check if the book is already issued
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM issued_book WHERE book_id = %s", [book_id]
                )
                existing_issue = cursor.fetchone()
                
                if existing_issue:
                    raise Exception("Book is already issued to a student.")

            # Get today's date as the issue date
            issue_date = date.today()

            # Execute SQL INSERT statement using cursor
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO issued_book (student_id, book_id, issue_date) VALUES (%s, %s, %s)",
                    [student_id, book_id, issue_date]
                )

            # Set success message
            messages.success(request, "Book issued successfully.")

            # Redirect to a success page or display a success message
            return redirect('issued_books', {'success_message': success_message})
        
        except Exception as e:
            # Handle any exceptions
            error_message = f"Error: {e}"
            return render(request, 'book_issue.html', {'error_message': error_message})

    else:
        # Render the form to issue a book
        return render(request, 'book_issue.html')

from django.db import  transaction

def return_book(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        book_id = request.POST.get('book_id')
        
        try:
            with transaction.atomic():
                # Check if the book is issued to the given student
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM issued_book WHERE student_id = %s AND book_id = %s",
                        [student_id, book_id]
                    )
                    issued_book = cursor.fetchone()

                if issued_book:
                    # Delete the record from issued books
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "DELETE FROM issued_book WHERE student_id = %s AND book_id = %s",
                            [student_id, book_id]
                        )

              
                else:
                    raise Exception("Book is not issued to this student")
            
            success_message = "Book returned successfully."

            # Redirect to a success page or display a success message
            return render(request, 'return_book.html', {'success_message': success_message})
        
        except Exception as e:
            # Handle any exceptions
            error_message = f"Error: {e}"
            return render(request, 'return_book.html', {'message': error_message})

    else:
        # Render the form to return a book
        return render(request, 'return_book.html')
