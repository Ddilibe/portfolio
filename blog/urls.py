#!/usr/bin/env python
""" Script for writing the urls for the blogs """

from django.urls import path, include
from blog import views

tagsurlpatterns = [
    path('', views.TagBlogListView.as_view(), name="all_blog_tags"), # Done this
    path('create/', views.TagBlogCreateView.as_view(), name="create_tag"), # Done this
    path('<str:name>/', views.TagBlogDetailView.as_view(), name="blog_tag_details"), # Done this
    path('<str:name>/edit', views.TagBlogUpdateView.as_view(), name="blog_tag_update"),
    path('<str:name>/remove', views.TagBlogDeleteView.as_view(), name="blog_tag_delete"),
]

blogurlpatherns = [
    path('tag/', include(tagsurlpatterns)),
    path('',views.BlogLandingView.as_view(), name="all_blog"), # Done this
    path('all/', views.BlogShowAllView.as_view(), name="blogs"),
    path('create/', views.BlogCreateView.as_view(), name="create_blog"), # Done this
    path('<str:name>/', views.BlogDetailView.as_view(), name="detail_blog"), # Done this
    path('<str:pk>/edit/', views.BlogUpdateView.as_view(), name="update_blog"), # Done this
    path('<str:name>/delete/', views.BlogDeleteView.as_view(), name="delete_blog"),
]

urlpatterns = [
    path('blog/', include(blogurlpatherns)),
]
