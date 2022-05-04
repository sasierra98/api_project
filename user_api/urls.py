from django.urls import path
from user_api.views.user import UserApiView, UserDetailView
from user_api.views.supplier import SupplierApiView, SupplierDetailView

urlpatterns = [
    path('user/', UserApiView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('supplier/', SupplierApiView.as_view()),
    path('supplier/<int:pk>', SupplierDetailView.as_view())
]
