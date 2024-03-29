"""banking_analytics URL Configuration

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
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from apps.core.views import AuthorPage, TeсhnologiesPage

handler404 = "apps.core.views.page_not_found"   # noqa
handler500 = "apps.core.views.server_error"     # noqa

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('apps.users.urls')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('about/', AuthorPage.as_view(), name='about'),
    path('teсhnologies/', TeсhnologiesPage.as_view(),
         name='teсhnologies'),
    path('banks/', include('apps.banks.urls', namespace='banks')),
    path('currency/', include('apps.currency.urls', namespace='currency')),
    path('api/', include('apps.api.urls')),
    path('news/', include('apps.news.urls', namespace='news')),
    path('cbrf/', include('apps.cbrf.urls', namespace='cbrf')),
    path('market/', include('apps.market.urls', namespace='market')),
    path('', include('apps.core.urls', namespace='core')),
]


urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
