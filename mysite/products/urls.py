from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.ProductMixinView.as_view()),  # detail
    # path('<int:pk>/update/', views.ProductMixinView.as_view()),  # update
    # path('<int:pk>/delete/', views.ProductMixinView.as_view()),  # delete
    # path('', views.ProductMixinView.as_view()),  # list / create

    path('<int:pk>/', views.ProductDetailAPIView.as_view()),  # detail
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),  # update
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),  # delete
    path('', views.ProductListCreateAPIView.as_view()),  # list / create

    # path('', views.product_list_create),
    # path('<int:pk>/', views.product_list_create),
]
