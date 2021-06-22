from django.contrib import admin
from django.urls import path
from enroll import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home')
]
