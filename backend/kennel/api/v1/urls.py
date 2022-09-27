from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import KennelViewSet

router = DefaultRouter()
router.register("kennel", KennelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
