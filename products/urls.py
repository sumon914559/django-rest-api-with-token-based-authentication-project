from django.urls import path
from .import views

urlpatterns = [
    path('products/', views.ShowAll,name='product-list'),
    path('product-detail/<int:pk>', views.ViewProduct,name='product-view'),
    path('product-create/', views.CreateProduct,name='create'),
    path('product-update/<int:pk>', views.UpdateProduct,name='product-update'),
    path('product-delete/<int:pk>', views.DeleteProduct,name='product-delete'),
    
]
