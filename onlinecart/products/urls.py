
from django.urls import path
from . import views
app_name='products'
urlpatterns = [
    path('product/<int:pk>',views.detailview, name='product_detail_view' ),
    path('wishlist/<int:pk>',views.addtowishlist, name='wishlist_detail_view'),
    path('wishlist/',views.Wishlistcbv.as_view(), name='wishlist'),
    path('wishlist/delete/<int:pk>',views.Deletewishlistcbv.as_view(), name='remove_wishlist_item')
]
