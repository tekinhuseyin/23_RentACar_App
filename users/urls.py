from django.urls import path,include
from .views import RegisterView

urlpatterns = [
    #login, logout
    path('auth/', include('dj_rest_auth.urls')),
    #register
    path('register/',RegisterView.as_view()),
]