from django.urls import path
from . import views

app_name='main'

urlpatterns=[
    path('signup/',views.index,name='sign_up'),
    path('logout/',views.logout,name='logout'),
    path('blog/',views.blog,name='blog'),
    path('',views.login,name='login'),
    path('post/',views.post,name='post1'),
    path('post/<int:pk>/',views.postD,name='postD'),
    path('create/',views.create,name='create'),
    path('update/<int:blog_id>/',views.update,name="update"),
    path('delete/<int:blog_id>/',views.delete,name='delete'),

]