from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DogViewSet

router = DefaultRouter()
router.register("dog", DogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
