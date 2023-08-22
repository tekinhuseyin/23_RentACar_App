"""
URL configuration for main project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
schema_view = get_schema_view(
    openapi.Info(
        title="Car Reservation API",
        default_version="v1",
        description="Car Reservation API project provides car and reservation info",
        terms_of_service="#",
        contact=openapi.Contact(email="nihalpolattekin@gmail.com"),  # Change e-mail on this line!
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
     # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    #for debug toolabar
    path('__debug__/', include('debug_toolbar.urls')),
    #my urls
    path('users/', include('users.urls')),
    path('', include('car.urls')),
]
from django.conf import settings
if settings.DEBUG:
        try:
            import debug_toolbar
            urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
        except ImportError:
            pass
# from django.conf.urls.static import static
# # url -> static-files-path:
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)