
from django.urls import path

from . import views

urlpatterns = [


    # Store main page

    path('', views.store, name='store'),


    # Ballot

    path('ballot', views.ballot, name='ballot'),

    # Ballot
    path('ballot_review<str:pk>', views.ballot_review, name='ballot_review'),

    #Table with confirmation

    path('table', views.table_conf, name='table_conf'),

    #Contact Page
    path('contact', views.contact, name='contact'),


    # Individual product

    path('product/<slug:product_slug>/', views.party_info, name='product-info'),


    # Individual category

    path('search/<slug:category_slug>/', views.list_category, name='list-category'),



    #Result page
     path('results', views.results, name='results'),


]














