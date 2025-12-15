from django.urls import path
from .views import ItemCreateAPIView, ItemListAPIView, ItemDetailAPIView

urlpatterns = [
    path('items/', ItemCreateAPIView.as_view(), name='item-create'),  # POST
    path('items/list/', ItemListAPIView.as_view(), name='item-list'),  # GET
    path('items/<int:item_id>/', ItemDetailAPIView.as_view()),  # PATCH, DELETE


]
