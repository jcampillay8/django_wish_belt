from django.urls import path
from . import views

urlpatterns = [    
    path('wish/home', views.home),
    # path('wish/authenticator', views.authenticator),
    path('wish/new', views.new),
    path('edit/<int:id>', views.edit),
    path('wish/stats', views.stats),
    path('logout', views.logout),
    path('wish/new_wish', views.new_wish),
    path('grant', views.grant),
    path('update/<int:id>', views.update),
    path('delete', views.delete),
    path('like', views.like),
]