# from django.contrib import admin
# from django.urls import path
# from home import views

# urlpatterns = [
#     path("", views.index , name = 'home'),
#     path("about", views.about, name = 'about'),
#     path("services" , views.services , name ="services"),
#     path("login" , views.user_register , name ="login"),
#     path('signin', views.signin , name= 'signin')

# ]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.starter, name='starter'),
    path('loginn/', views.user_login, name='loginn'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('addbook/', views.add_book, name='addbook'),
    # path('ava_books/<int:pk>', views.book_record, name='ava_books'),
    path('ava_books/', views.all_books, name='ava_books'),
    path('search_books/', views.search_books, name='search_books'),
    path('student_reg/', views.student_reg, name = 'student_reg'),
    path('student_login/', views.Stud_login, name='student_login'),
    path('display_table/', views.display_table, name='display_table'),
    path('new_reg/', views.register_student, name='new_reg'),
    # path('issue_book/<int:book_id>/', views.issue_book, name='issue_book'),
    path('issued_books', views.issued_books, name='issued_books'),
    path('book_issue', views.issue_book, name='book_issue'),
    path('return_book', views.return_book, name='return_book')

]