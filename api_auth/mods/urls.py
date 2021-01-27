from django.urls import path
from mods import views

urlpatterns = [
    # Return 'Mods' model objects
    path('mods/', views.ModsView.as_view(), name='mods_view')
]
