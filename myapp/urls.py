
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('signup/',views.signup),
    path('forgotpass/',views.forgotpass),
    path('home/',views.home,name='home'),
    path('about/',views.about),
    path('contact/',views.contact),
    path('profile/',views.profile),
    path('addblog/',views.addblog),
    path('login/',views.login),
    path('logout/',views.logout),
    path('add/', views.add_blog, name='add_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),



]
