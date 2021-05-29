from django.urls import path
from . import views

urlpatterns = [    
    path('wish/home', views.home),
    # path('hacker', views.hacker),
    # path('new', views.new),
    # path('edit/<int:id>', views.edit),
    # path('stats', views.stats),
    # path('logout', views.logout),
    # path('new_wish', views.new_wish),
    # path('grant', views.grant),
    # path('update/<int:id>', views.update),
    # path('delete', views.delete),
    # path('like', views.like)
]