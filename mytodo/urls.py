from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoItemViewSet
<<<<<<< HEAD
from .views import SecureHelloView
=======
>>>>>>> 133d20b5e619d853b1e1220cca41449c4eb4a9bf

router = DefaultRouter()
router.register(r'mytodo', ToDoItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
<<<<<<< HEAD
    path('secure-hello/', SecureHelloView.as_view()),
=======
>>>>>>> 133d20b5e619d853b1e1220cca41449c4eb4a9bf
]