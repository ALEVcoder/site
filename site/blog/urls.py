from django.urls import path
from . import views
from .views import BlogListView,BlogCreateView,BlogDetailView,BlogUpdateView,BlogDeleteView,HosilView,TView
urlpatterns = [
    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='post_delete'),
    path("post/<int:pk>/edit",BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('',BlogListView.as_view(),name='home'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('post/new/None',HosilView.as_view(),name='hsl'),
    path('post/17/None',TView.as_view(),name='thr')
]