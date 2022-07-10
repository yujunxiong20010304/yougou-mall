from pathlib import Path
from datetime import timedelta
import datetime
import os
from Crypto import Random
from Crypto.PublicKey import RSA
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)olhbbdn!b3&=bb0recxio*)v#&lpic**uo0!*)!+e098gfov0'
# 支付宝配置
APP_PRIVATE_KEY = open(os.path.join(BASE_DIR, "shop/keys/app_private_key.pem"), 'r').read()
ALIPAY_PUBLIC_KEY = open(os.path.join(BASE_DIR, "shop/keys/alipay_public_key.pem"), 'r').read()
ALIPAY_APP_ID = '2021000121602053'
RETURN_URL = 'http://localhost:8080/'
GATEWAY = "https://openapi.alipaydev.com/gateway.do?"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 前后端数据加密
# 伪随机数的方式生成RSA公私钥对
random_generator = Random.new().read
rsa = RSA.generate(1024, random_generator)
# 私钥
pri_key = rsa.exportKey().decode('utf-8')
# 公钥
pub_key = rsa.publickey().exportKey().decode('utf-8')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth.apps.OauthConfig',  # 用户认证
    'rest_framework',  # 使用Django rest framework
    'rest_framework.authtoken',  # token
    'corsheaders',  # 跨域访问设置
    'captcha',  # 图形验证码配置
    'store.apps.StoreConfig',  # 商店
    'payment.apps.PaymentConfig',  # 支付
    'user.apps.UserConfig',
]

# 增加跨域忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# 允许所有方法
CORS_ALLOW_METHODS = '*'
# 允许所有请求头
CORS_ALLOW_HEADERS = '*'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# 链接mysql数据库
DATABASES = {
    # 默认mysql数据库
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': '47.109.23.208',
        'PORT': '3306',
    }
}
'''# 链接redis数据库/redis数据库缓存配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://47.109.23.208:6379/",
        "OPTIONS": {
            "PASSWORD": 'yjx20010304',
            "DB": 5,
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "IGNORE_EXCEPTIONS": True,
        }
    }
}
'''
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 指定用户数据库认证表
AUTH_USER_MODEL = "oauth.User"

REST_FRAMEWORK = {
    # DEFAULT_PERMISSION_CLASSES设置默认的权限类，通过认证后赋予用户的权限
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    # DEFAULT_AUTHENTICATION_CLASSES设置默认的认证类，这里用token，也可以设置session或自定义的认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # 进行token认证
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    )
}

# SIMPLE_JWT是token配置项，参数很多，不一一列举，请自查……^ ^
# 导入datetime库生成时间参数
SIMPLE_JWT = {
    # ACCESS_TOKEN_LIFETIME设置token令牌有效时间
    # rest_framework_simplejwt官方默认有效时间是5分钟，这里改成15天
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),  # days=15
    # REFRESH_TOKEN_LIFETIME设置token刷新令牌有效时间
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer', 'JWT'),
    # 是否可刷新
    'JWT_ALLOW_REFRESH': True,
}

# 邮箱
EMAIL_HOST = 'smtp.qq.com'  # 发送邮件的域名
# 设置端口号,为数字
EMAIL_PORT = 25
# 设置发件人邮箱
EMAIL_HOST_USER = '2140585762@qq.com'
# 设置发件人的邮箱授权码
EMAIL_HOST_PASSWORD = 'ealpjsmghjfufacd'
# 设置是否启用安全链接
EMAIL_USER_TLS = True
# 收件人看到的发件人
EMAIL_FROM = '优购<2140585762@qq.com>'

# 图形字母验证码
CAPTCHA_IMAGE_SIZE = (150, 48)  # 设置 captcha 图片大小
CAPTCHA_LENGTH = 4  # 字符个数
CAPTCHA_TIMEOUT = 1  # 超时(minutes)
# 图像验证码格式，可以自定义。
CAPTCHA_OUTPUT_FORMAT = u'%(text_field)s  %(image)s %(hidden_field)s'
# 添加干扰点、干扰线
CAPTCHA_NOISE_FUNCTIONS = (
    'captcha.helpers.noise_null',
    'captcha.helpers.noise_arcs',  # 干扰线
    'captcha.helpers.noise_dots',  # 干扰点
)
# 背景颜色
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
# 验证码的样式
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'  # 随机字符
