from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views

urlpatterns = [
    path('Restaurant-List/', views.RestaurantList.as_view()),
    path('Restaurant-Detail/<int:pk>/', views.RestaurantDetail.as_view()),
    
    path('Category-List/', views.CatagoryList.as_view()),
    path('Category-Detail/<int:pk>/', views.CategoryDetail.as_view()),
    
    path('Food-List/', views.FoodList.as_view()),
    path('Food-Detail/<int:pk>/', views.FoodDetail.as_view()),
    
    path('Catagory/<int:id>/', views.get_catagory1),
    
    path('Restaurant/<int:id>/', views.get_restaurant1),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)