"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from django.views import static
from django.conf import settings
from django.conf.urls import url, include

from rest_framework import routers
from article.urls import urlpatterns as article_urls
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .mock_view import mock_urls
from . import views


schema_view = get_schema_view(

    openapi.Info(
        title="Demo API",
        default_version='v1',
        description="Demo description",
        terms_of_service="",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

swagger_urls = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# drf 视图演示
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    url(r'^', include(router.urls)),
    path('api/', include(article_urls)),
    url(r'^jwt-token-verify/', verify_jwt_token),
    url(r'^jwt-token-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # url('^schema/$', schema_view),
    re_path(r"^static/(?P<path>.*)$", static.serve, {"document_root": settings.STATIC_ROOT}, name="static",),
]

urlpatterns = urlpatterns + mock_urls + swagger_urls
