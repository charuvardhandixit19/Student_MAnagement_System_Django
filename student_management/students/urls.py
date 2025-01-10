from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('show_students/', views.show_students, name='show_students'),
    path('search/', views.search_student, name='search_student'),
#    path('update/', views.update_student, name='update_student'),  # General update page with no ID required
    # path('update/<int:id>/', views.update_student, name='update_student_with_id'),
    path('update-student/', views.update_student, name='update_student'),
    path('delete/', views.delete_student, name='delete_student'),
]

