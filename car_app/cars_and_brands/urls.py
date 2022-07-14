from django.urls import path
from . import views

urlpatterns = {
    path('',views.index),
    path('brands/', views.brands), # a list of all the car brands
    path('brands/new/', views.add_brand), # form for a new car brand
    # path('brands/<:id>/'), # see a specific car brand
    # path('brands/<:id>/edit/'), # edit page for a specific car brand

    # path('brands/<:brand_id>/cars/'), # a list of cars for a specific car brand
    # path('brands/<:brand_id>/cars/new/'), # form for a new car under a specific car brand
    # path('brands/<:brand_id>/cars/<:car_id>/'), # see a specific car for a specific car brand
    # path('brands/<:brand_id>/cars/<:car_id>/edit/'), # edit page for a specific car under a specific car brand
}