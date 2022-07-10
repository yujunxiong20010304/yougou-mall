from django.urls import path
from . import views

urlpatterns = [
    path('upimage/', views.UploadImage.as_view(), name='upimage'),
    path('shopcart/', views.ShopCart.as_view(), name='shopcart'),
    path('delete_shop_cart/', views.deleteShopCart.as_view(), name='delete_shop_cart'),
    path('evaluated/', views.Evaluated.as_view(), name='evaluated'),
    path('address/', views.GetUserAddress.as_view(), name='GetUserAddress'),
    path('delete_address/', views.DeleteAddress.as_view(), name='delete_address'),
    path('confirm_receipt/', views.ConfirmReceipt.as_view(), name='confirm_receipt'),
    path('user_information/', views.UserInformationDisplay.as_view(), name='user_information'),
    path('user_repeat/', views.UserRepeat.as_view(), name='user_repeat'),
    path('update_user_info/', views.UpdateUserInfo.as_view(), name='update_user_info'),
    path('send_email/', views.SendEmail.as_view(), name='send_email'),
    path('comment/', views.Comment.as_view(), name='comment'),
]
