from django.urls import path
from . import views
urlpatterns = [
    path('user/', views.userInfo.as_view(), name='userInfo'),
    path('shopping/', views.ShoppingInfo.as_view(), name='ShoppingInfo'),
    path('goods/', views.goodsInfo, name='goodsInfo'),
    path('detail/', views.shopDetailInfo, name='shopDetailInfo'),
    path('update/', views.updatePrice, name='updatePrice'),
    path('address/', views.getAddress, name='getAddress'),
    path('obtainShop/', views.obtainShop.as_view(), name='obtainShop'),
    path('search/', views.Search.as_view(), name='search'),
    path('brands/', views.brand, name='brand'),
    path('show_comment/', views.show_comment, name='show_comment'),
]
