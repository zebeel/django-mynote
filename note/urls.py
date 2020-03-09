from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('save_note', views.save_note, name='save_note'),
    path('edit/<int:note_id>', views.edit, name='edit'),
    path('delete/<int:note_id>', views.delete, name='delete'),
]
