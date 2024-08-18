
from django.contrib import admin
from django.urls import path, include
from users import views as userVievs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', userVievs.register, name='reg'),
    path('', include('jeans.urls')),
]
