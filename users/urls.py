from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('register/', views.SignupUser, name='register'),
    path('edit-account/', views.editAccount, name='edit-account'),
    
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
