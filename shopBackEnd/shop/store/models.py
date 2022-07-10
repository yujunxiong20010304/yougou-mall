from django.db import models
from oauth.models import User
from django.utils.timezone import now


# 城市表
class City(models.Model):
    id = models.BigAutoField('主键', primary_key=True)
    name = models.CharField('城市名字', max_length=25)
    parent_id = models.IntegerField('父id', null=True, blank=True)
    type = models.IntegerField('级别')

    class Meta:
        db_table = 'city'


# 商品总类表
class Goods(models.Model):
    id = models.BigAutoField(primary_key=True)  # 商品的主键
    store = models.CharField('店铺的名称', max_length=125)  # 品牌名称
    score = models.IntegerField('商品得分', default=100)  # 由用户评价等级最后得出的分数
    goods_parameter = models.TextField('商品参数信息')
    title = models.CharField(max_length=225)  # 商品名称
    goods_image = models.TextField('展示图片')  # 展示图片
    image_parameter = models.TextField('图片介绍')  # 将图片地址保存为字符串
    shop = models.CharField(max_length=225)  # 店铺名称

    class Meta:
        db_table = 'goods'


class OptName(models.Model):
    id = models.BigAutoField(primary_key=True)  # id
    name = models.CharField(max_length=225)  # 配置名称

    class Meta:
        db_table = 'opt_name'


# 商品详细选择
class Opt(models.Model):
    STATUS = (
        (0, '删除'),
        (1, '存在')
    )
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(OptName, on_delete=models.CASCADE)
    image = models.CharField(max_length=225, null=True)
    content = models.CharField(max_length=225)
    create_date = models.DateTimeField('创建配置的时间', default=now)
    modify_date = models.DateTimeField('修改时间', default=now)
    status = models.IntegerField('存在状态', choices=STATUS, default=1)
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)

    class Meta:
        db_table = 'opt'
