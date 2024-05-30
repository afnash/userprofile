from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_view,name='index'),
    path('signup/',views.sign_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('info/',views.info,name='info'),
    path('success/',views.success_view,name='success'),
    path('logout/',views.logout_view,name='logout'),

]