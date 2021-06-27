from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include("users.urls", namespace="login")),
    path('road/', include("roads.urls", namespace="road")),
]
