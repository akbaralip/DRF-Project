
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_list.urls')),
    path('director-list/', include('director_list.urls')),
]
