from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('oauth.urls')),  # 用户认证页
    path('captcha/', include('captcha.urls')),  # 图片验证码使用
    path('store/', include('store.urls')),  # 商品页
    path('payment/', include('payment.urls')),  # 支付
    path('user/', include('user.urls')),
]
