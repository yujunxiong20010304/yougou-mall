from django.urls import path
from . import views
urlpatterns = [
    path('storeInfo/', views.StoreInfo.as_view(), name='storeInfo'),
    path('addAddress/', views.AddUserAddress.as_view(), name='addAddress'),
    path('sureOrder/', views.SureOrder.as_view(), name='sureOrder'),
    path('sandbox_payment/', views.SandboxPayment.as_view(), name='SandboxPayment'),
    path('orderInfo/', views.OrderInfo.as_view(), name='orderInfo'),
    path('surePayment/', views.SurePayment.as_view(), name='surePayment'),
    path('address_validate/', views.ValidateAddress.as_view(), name='address_validate'),
    path('shop_cart_order/', views.ShopCartOrder.as_view(), name='shop_cart_order'),
    path('alipay_return/', views.alipay_return)
]
