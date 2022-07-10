from django.urls import path, include, re_path
from . import views
# 导入 simplejwt 提供的几个验证视图类
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'oauth'

urlpatterns = [
    # 接口测试
    # 使用自定义的视图进行登录
    path('login/', views.LoginView.as_view()),
    # 公钥
    path('public_key/', views.givePublicKey, name='give_key'),
    # 图形验证码
    path('refresh_captcha/', views.refresh_captcha, name='refresh_captcha'),
    # DRF 提供的一系列身份认证的接口，用于在页面中认证身份，详情查阅DRF文档
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 获取Token的接口
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新Token有效期的接口
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 验证Token的有效性
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', views.Register.as_view()),
    re_path(r'^active/(?P<token>.*)$', views.ActiveView.as_view(), name='active'),  # 用户激活
]
