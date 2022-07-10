from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 购物车，由用户与商品多对多产生
class User(AbstractUser):
    STATE = (
        (0, '未激活'),
        (1, '激活')
    )
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('用户名', max_length=20, unique=True, db_column='username')
    password = models.CharField('密码', max_length=88, db_column='password')
    email = models.CharField('邮箱', max_length=225, unique=True, db_column='email')
    # 本地存储图片，保存拼凑的图片地址
    head_portrait = models.CharField('头像', default='https://wwc.alicdn.com/avatar/getAvatar.do?userNick=tb758136261',
                                     max_length=225, db_column='head_portrait')
    delete_portrait = models.CharField('删除头像', max_length=225, null=True)
    balance = models.IntegerField('余额', default=10000, db_column='balance')
    payPassword = models.CharField('支付密码', max_length=25, blank=True, null=True)
    is_active = models.IntegerField('状态', choices=STATE, default=0, db_column='is_active')
    created_time = models.DateTimeField('创建时间', default=now, db_column='creat_time')
    last_mod_time = models.DateTimeField('修改时间', default=now, db_column='last_time')
    introduce = models.CharField('用户的个人简介', default='普通人', max_length=255)

    class Meta:
        db_table = 'user'
