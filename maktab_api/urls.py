"""
URL configuration for maktab_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.conf import settings 
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="API Hujjatlari",
        default_version='v1',
        description="API uchun hujjatlar",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path("oquvchi/", include("oquvchi.urls")),
    path("maktab/", include("maktab.urls")),
    path("kirishlar/", include("kirishlar.urls")),
    path("ega/", include("ega.urls")),
    path("mbadmin/", include("maktabadmin.urls")),

    path("swagger.json", schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("teleusers/", include("teleusers.urls")),
    path("telegroups/", include("telegroups.urls")),
    path("chiqish/", include("chiqish.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)