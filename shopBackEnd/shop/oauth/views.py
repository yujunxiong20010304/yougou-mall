from django.http import HttpResponse, JsonResponse
from oauth.models import User
import json
from django.views import View
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase, TokenObtainPairView
from .serializers import MyTokenSerializer
# APIView是REST framework提供的所有视图的基类,
# 继承自Django的View，对Django中的View进行了拓展，
# 具备了认证、授权、限流、不同请求数据的解析的功能。
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from shop import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired
from django.core.mail import send_mail
from django.shortcuts import redirect
from shop.settings import pri_key, pub_key
from utils.rsa_crypt import decrypt_data


# 自定义的登陆视图
class LoginView(TokenViewBase):
    serializer_class = MyTokenSerializer  # 使用刚刚编写的序列化类

    # post方法对应post请求，登陆时post请求在这里处理
    def post(self, request, *args, **kwargs):
        # 在这里做一个拦截进行验证码的识别处理
        data = json.loads(request.body)
        username = data.get('username', None)
        password = data.get('password', None)
        password = decrypt_data(password, pri_key)
        request.data['password'] = password
        verification = data.get('hashKey', None)  # 用户提交的验证码
        key = data.get('key', None)  # 验证码答案
        user = authenticate(username=username, password=password)
        if not user:
            return JsonResponse({"code": 404, "msg": "用户名与密码不匹配", "status": 0, "data": {}})
        if not jarge_captcha(key, verification):
            return JsonResponse({"code": 404, "msg": "验证码不匹配", "status": 1, "data": {}})
        # 使用刚刚编写时序列化处理登陆验证及数据响应
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            return JsonResponse({"code": 404, "msg": "fail", "data": {}})
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


# 验证码
# 刷新验证码
def refresh_captcha(request):
    return HttpResponse(json.dumps(captchas()), content_type='application/json')


# 创建验证码
def captchas():
    hashkey = CaptchaStore.generate_key()  # 验证码答案
    image_url = captcha_image_url(hashkey)  # 验证码地址
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha


# 验证验证码是否正确
def jarge_captcha(captchaStr, captchaHashkey):
    if not (captchaStr and captchaHashkey):
        return False
    # 获取根据hashkey获取数据库中的response值
    # get_captcha = get_object_or_404(CaptchaStore, hashkey=captchaHashkey)
    get_captcha = CaptchaStore.objects.filter(hashkey=captchaHashkey)
    if not get_captcha:
        return False
    if get_captcha[0].response == captchaStr.lower():  # 如果验证码匹配
        return True


class Register(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        username = data.get('username', None)
        password = data.get('password', None)
        password = decrypt_data(password, pri_key)
        email = data.get('email', None)
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        serializer = Serializer(settings.SECRET_KEY, 3600)  # 加密方式，加密时间
        info = {'confirm': user.id}  # 获取用户id
        token = serializer.dumps(info)  # 对用户id进行加密
        token = token.decode()  # 默认加密后是byte类型，解密为utf8
        html_message = """<h1>%s,优购欢迎您的到来</h1>请点击以下链接进行激活<br/>
                                <a href="http://127.0.0.1:8000/oauth/active/%s">点击我进行激活</a>""" % (username, token)
        res = send_mail('优购', '', settings.EMAIL_FROM, [email], html_message=html_message)
        if res == 1:
            return JsonResponse({'code': 200, 'msg': 'success', 'data': {}})
        else:
            return JsonResponse({'code': 200, 'msg': 'fail', 'data': {}})


class ActiveView(View):
    @staticmethod
    def get(request, token):
        # 对用户信息进行解密
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            user_id = info['confirm']  # 获取解密id
            user = User.objects.get(id=user_id)  # 获取用户信息
            user.is_active = 1  # 激活
            user.save()
            # 跳转到登陆页面
            return redirect('http://localhost:8080/oauth/login/')
        except SignatureExpired as e:
            return HttpResponse(status=404, content='对不起，激活时间过期')


# 密码加密的公钥
def givePublicKey(request):
    return JsonResponse({'code': 200, 'msg': 'success', 'data': pub_key})
