from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('', views.ProductListCreateAPIView.as_view()),

    # path('', views.product_list_create),
    # path('<int:pk>/', views.product_list_create),
]
