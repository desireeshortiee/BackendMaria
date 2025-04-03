from django.contrib import admin
from django.urls import path, include
from .views import HomePageView  # Add the HomePageView here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mytodo.urls')),
    path('', HomePageView.as_view(), name='home'),  # This will handle the root URL
]
