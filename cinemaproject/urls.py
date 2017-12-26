
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cinemas.urls')),
    path('cinemas/', include('cinemas.urls')),

]
