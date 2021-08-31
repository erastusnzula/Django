from django.urls import path

from item import views

app_name = 'item'
urlpatterns = [
    path('item/', views.all_items, name='all-items'),
    path('item/<int:id>/', views.item_detail, name='item-detail'),
    path('item/<category>/', views.item_category, name='item-category'),
    path('add/<int:id>/', views.add_to_cart, name='add-to-cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove_cart/<int:id>/', views.remove_from_cart_summary, name='remove-from-cart-summary'),
    path('decrease/<int:id>/', views.decrease_item_quantity_from_cart, name='decrease-quantity'),
    path('increase/<int:id>/', views.increase_item_quantity_from_cart, name='increase-quantity'),
    path('item/cart', views.cart_items, name='cart'),
]
