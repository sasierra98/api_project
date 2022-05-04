from django.urls import path
from product_api.views.category import CategoryView, DetailCategoryView
from product_api.views.product import ProductView, DetailProductView

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('product/<int:pk>', DetailProductView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>', DetailCategoryView.as_view())
]
