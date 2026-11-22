from django.contrib import admin
from django.urls import path, include, re_path
# from

urlpatterns = [
    path('', include('courses.urls')),
    path('admin/', admin_site),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
