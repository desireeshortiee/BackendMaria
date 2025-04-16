from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from mytodo.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mytodo.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('api-token-auth/', obtain_auth_token),  # ✅ Direct token path
]
