from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Campus Voice",
        default_version="v0.1",
        description="Engine behind the Campus Voice",
        contact=openapi.Contact(email="kingosenitosin@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Campus Voice API Admin"

admin.site.site_title = "Campus Voice API Admin Portal"

admin.site.index_title = "Welcome to Campus Voice API Portal"
