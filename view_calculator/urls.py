
from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('odd_or_even/<int:number>/', views.odd_or_even)
]
