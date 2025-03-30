"""
URL configuration for masterointeriors project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


# masterointeriors/urls.py
from django.contrib import admin
from django.urls import path
from mastero_interiors import views as mastero_views
from mastero_interiors import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', mastero_views.mastero_interiors, name='index'),
    path('blog', mastero_views.blog_page, name='blog_page'),
    path('blog/<int:pk>/', mastero_views.blog_page, name='blog_page'),
    # path('blog/<int:post_id>/', views.blog_page, name='blog_detail'),  # URL pattern for blog detail

    path('create/', views.create_blog_post, name='create_blog_post'),
    path('bloglist/', views.blog_list, name='blog_list'),  # URL pattern for the blog list
    path('custom_edit_blog_post/<int:pk>/', views.custom_edit_blog_post, name='custom_edit_blog_post'),


    # Your other URL patterns here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
