from django.contrib import admin
from django.urls import path, include
from .views import HomePageView  # Add the HomePageView here
<<<<<<< HEAD
from rest_framework.authtoken.views import obtain_auth_token
=======
>>>>>>> 133d20b5e619d853b1e1220cca41449c4eb4a9bf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mytodo.urls')),
    path('', HomePageView.as_view(), name='home'),  # This will handle the root URL
<<<<<<< HEAD
    path('api-token-auth/', obtain_auth_token),
=======
>>>>>>> 133d20b5e619d853b1e1220cca41449c4eb4a9bf
]
