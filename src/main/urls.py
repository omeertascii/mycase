from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet


schema_view = get_schema_view(
    openapi.Info(
        title = "Discord API",
        default_version = "v1",
        description = "A simple Discord API",
        terms_of_service = "https://www.example.com/terms/",
        contact = openapi.Contact(email = "contact@example.com"),
        license = openapi.License(name = "BSD License"),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]