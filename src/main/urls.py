from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExampleView

router = DefaultRouter()
router.register(r'workgroups', ExampleView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),

    path('', include(router.urls)),
    ]