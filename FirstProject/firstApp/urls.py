from django.urls import path
from firstApp import views as fa

urlpatterns = [
    path('hello/', fa.display,name='display'),
    path('datetime/',fa.displayDateTime,name='displayDateTime'),
]