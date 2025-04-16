from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoItemViewSet
from .views import SecureHelloView

router = DefaultRouter()
router.register(r'mytodo', ToDoItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('secure-hello/', SecureHelloView.as_view()),
]