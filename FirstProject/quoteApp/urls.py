from django.urls import path
from quoteApp import views as qa

urlpatterns = [
    path('quote/',qa.displayQuote,name='displayQuote'),
]