from django.contrib import admin
from django.urls import path, include
from .views import HomePageView  # Add the HomePageView here
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mytodo.urls')),
    path('', HomePageView.as_view(), name='home'),  # This will handle the root URL
    path('api-token-auth/', obtain_auth_token),
]
