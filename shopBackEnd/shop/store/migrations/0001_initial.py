# Generated by Django 3.2 on 2022-07-03 06:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('name', models.CharField(max_length=25, verbose_name='城市名字')),
                ('parent_id', models.IntegerField(blank=True, null=True, verbose_name='父id')),
                ('type', models.IntegerField(verbose_name='级别')),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('store', models.CharField(max_length=125, verbose_name='店铺的名称')),
                ('score', models.IntegerField(default=100, verbose_name='商品得分')),
                ('goods_parameter', models.TextField(verbose_name='商品参数信息')),
                ('title', models.CharField(max_length=225)),
                ('goods_image', models.TextField(verbose_name='展示图片')),
                ('image_parameter', models.TextField(verbose_name='图片介绍')),
                ('shop', models.CharField(max_length=225)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='OptName',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
            ],
            options={
                'db_table': 'opt_name',
            },
        ),
        migrations.CreateModel(
            name='Opt',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=225, null=True)),
                ('content', models.CharField(max_length=225)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建配置的时间')),
                ('modify_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('status', models.IntegerField(choices=[(0, '删除'), (1, '存在')], default=1, verbose_name='存在状态')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.goods')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.optname')),
            ],
            options={
                'db_table': 'opt',
            },
        ),
    ]
