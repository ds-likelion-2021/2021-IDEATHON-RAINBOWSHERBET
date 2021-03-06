from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls", namespace="users")),
    path('road/', include("roads.urls", namespace="road")),
    path('upload/', include("roads.urls", namespace="upload")),
]
