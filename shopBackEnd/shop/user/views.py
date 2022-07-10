from utils.token_verify import MyApiView  # 被修改了内部函数的APIView
from oauth.models import User
from payment.models import ShoppingCart, Price, Receiving
from store.models import Goods
from django.http import JsonResponse
from utils.data_process import data_conversion, sendMessage, text_description_configure, paging
import json
from django.db.models import Q
from django.views.generic import View
import requests
from payment.models import Assess
from shop.settings import pri_key
from utils.rsa_crypt import decrypt_data

# Create your views here.


# 图片跟换头像效果展示
class UploadImage(MyApiView):
    @staticmethod
    def post(request):
        file = request.data.get('file')
        user_id = request.user.id
        headers = {'Authorization': 'hAoKC0DEfS50wEGzAPQelw2v1XjM14oX'}
        files = {'smfile': file}
        url = 'https://sm.ms/api/v2/upload'
        res = requests.post(url, files=files, headers=headers).json()
        if res['code'] != 'success':
            return JsonResponse({'code': 404, 'msg': 'fail', 'data': {}})
        delete_portrait = request.user.delete_portrait  # 删除图片的链接地址
        url = res['data']['url']
        delete_image = res['data']['delete']
        if delete_portrait:
            res = requests.get(delete_portrait).text
        User.objects.filter(id=user_id).update(head_portrait=url, delete_portrait=delete_image)
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {'url': url}})


# 购物车信息查询
class ShopCart(MyApiView):
    @staticmethod
    def post(request):
        user_id = request.user.id
        data = json.loads(request.body)
        types = data.get('type')
        index = data.get('index')
        # 需要做的查询步骤
        # 根据用户id查询出购物车的信息，根据购物车中的价格id推导出商品信息
        data_count = ShoppingCart.objects.filter(Q(user_id=user_id) & Q(status=types)).count()
        shop_cart = None
        if index:
            page = paging(data_count, index, 5)
            start_index = page.get('start_index')
            end_index = page.get('end_index')
            page_count = page.get('page_count')
            shop_cart = ShoppingCart.objects.filter(Q(user_id=user_id) & Q(status=types)).order_by('-modify_date').values(
                'num', 'price_id', 'id',
                'create_date')[start_index:end_index]
        else:
            shop_cart = ShoppingCart.objects.filter(Q(user_id=user_id) & Q(status=types)).order_by(
                '-modify_date').values(
                'num', 'price_id', 'id',
                'create_date')
        shop_cart_info = []
        for shop in shop_cart:
            num = shop.get('num')  # 数量
            price_id = shop.get('price_id')
            price = Price.objects.filter(id=price_id).values('price', 'goods_id').first()
            good_id = price.get('goods_id')
            good = Goods.objects.filter(id=good_id).values('shop', 'store', 'title', 'goods_image')
            good = data_conversion(good)
            result = {'num': num, 'price': price.get('price'), 'id': shop.get('id'), 'selected': 'false',
                      'time': shop.get('create_date'), 'opts': text_description_configure(price_id)}
            result.update(good[0])
            result = {'shop': result['shop'], 'content': [result], 'select': 'false'}
            if types == 1:
                if not shop_cart_info:
                    shop_cart_info.append(result)
                else:
                    judge = True
                    for i in shop_cart_info:
                        if i['shop'] == result['shop']:
                            i['content'].append(result['content'][0])
                            judge = False
                    if judge:
                        shop_cart_info.append(result)
            else:
                shop_cart_info.append(result)
        if types == 1:
            return JsonResponse({'code': 200, 'msg': 'success',
                                 'data': {'shop_cart_info': shop_cart_info}})
        return JsonResponse(
            {'code': 200, 'msg': 'success', 'data': {'shop_cart_info': shop_cart_info, 'page_count': page_count}})


class deleteShopCart(MyApiView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        shop_cart_id = data.get('id')
        ShoppingCart.objects.filter(id=shop_cart_id).update(status=0)
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {}})


class Evaluated(MyApiView):
    @staticmethod
    def post(request):
        user_id = request.user.id
        shop_cart = ShoppingCart.objects.filter(
            Q(user_id=user_id) &
            Q(is_assess=0) &
            Q(status=5)).values('receiving', 'price_id', 'id', 'modify_date', 'num')
        evaluate = []
        for shop in shop_cart:
            name = Receiving.objects.filter(id=shop['receiving']).values('name')[0]
            price = Price.objects.filter(id=shop['price_id']).first()
            title = price.goods_id.title
            img = eval(price.goods_id.goods_image)[0]
            result = {'name': name['name'], 'title': title, 'img': img, 'price': price.price, 'num': shop['num'],
                      'id': shop['id']}
            evaluate.append(result)
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {'evaluate': evaluate}})


class GetUserAddress(MyApiView):
    @staticmethod
    def post(request):
        user_id = request.user.id
        city_address = Receiving.objects.filter(Q(user_id=user_id) & Q(state=1)). \
            values('id', 'name', 'phone', 'city_address', 'detailed_address', 'postal_code')
        for i in city_address:
            i['city_address'] = eval(i.get('city_address'))
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {'city_address': list(city_address)}})


class DeleteAddress(MyApiView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        id = data.get('id')
        Receiving.objects.filter(id=id).update(state=0)
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {}})


# 确认收货
class ConfirmReceipt(MyApiView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        id = data.get('id').split('.')
        for i in id:
            ShoppingCart.objects.filter(id=i).update(status=5)
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {}})


# 用户信息展示
class UserInformationDisplay(MyApiView):
    @staticmethod
    def post(request):
        user_id = request.user.id
        password = request.user.password
        print(password)
        user_info = User.objects.filter(id=user_id).values('username', 'email', 'head_portrait', 'payPassword',
                                                           'introduce').first()
        print(user_info)
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {'user_info': user_info}})


# 用户信息判断是否重复
class UserRepeat(View):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        value = data.get('value')
        only = data.get('only')
        if only == 0:
            print(0)
            test = User.objects.filter(username=value).first()
            if not test:
                return JsonResponse({'code': 200, 'msg': 'success', 'state': 1})
        elif only == 1:
            if request.user.check_password(value):
                return JsonResponse({'code': 200, 'msg': 'success', 'state': 1})
        elif only == 2:
            test = User.objects.filter(email=value).first()
            if not test:
                return JsonResponse({'code': 200, 'msg': 'success', 'state': 1})
        return JsonResponse({'code': 200, 'msg': 'success', 'state': 0})


# 更新用户信息
class UpdateUserInfo(MyApiView):
    @staticmethod
    def post(request):
        user_id = request.user.id
        data = json.loads(request.body)
        basic = data.get('basic')
        password = data.get('password')
        email = data.get('email')
        if basic:
            User.objects.filter(id=user_id).update(username=basic['username'], introduce=basic['description'],
                                                   payPassword=basic['payment'])
        if password:
            user = request.user
            password = decrypt_data(password, pri_key)
            user.set_password(password['NewPassword'])
            user.save()
        if email:
            User.objects.filter(id=user_id).update(email=email['email'])
        user_info = User.objects.filter(id=user_id).values('username', 'email', 'head_portrait', 'payPassword',
                                                           'introduce').first()
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {'user_info': user_info}})


# 发送邮箱验证码
class SendEmail(MyApiView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        email = data.get('email')
        # 验证码
        verification_code = ''
        try:
            verification_code = sendMessage(email)
            msg = 'success'
        except:
            msg = 'fail'
        return JsonResponse({'code': 200, 'msg': msg, 'data': {'verification_code': verification_code}})


# 商品评价
class Comment(MyApiView):
    def post(self, request):
        data = json.loads(request.body)
        comment = data.get('textarea')
        score = data.get('score')
        if not comment:
            return JsonResponse({'code': 404, 'msg': 'fail', 'data': ''})
        user_id = request.user.id
        id = data.get('id')  # 购物车id
        goods_id = data.get('goods_id')
        ShoppingCart.objects.filter(Q(id=id) & Q(user_id=user_id)).update(is_assess=1)
        Assess.objects.create(content=comment, grade=score, type=0, state=1, goods_id_id=goods_id, user_id_id=user_id)
        return JsonResponse({'code': 200, 'msg': 'success', 'data': ''})

    def get(self, request):
        data = request.GET
        id = data.get('id')
        user_id = request.user.id
        if not (id and user_id):
            return JsonResponse({'code': 404, 'msg': 'fail', 'data': ''})
        shop_cart = ShoppingCart.objects.filter(Q(id=id) & Q(user_id=user_id) & Q(is_assess=0) & Q(status=5)).values(
            'price_id').first()
        if not shop_cart:
            return JsonResponse({'code': 404, 'msg': 'fail', 'data': ''})
        price_id = shop_cart.get('price_id')
        test = Price.objects.filter(id=price_id).first()
        price = test.price  # 商品价格
        goods_id = test.goods_id.id
        title = test.goods_id.title  # 商品的名字
        img = test.goods_id.goods_image  # 商品展示的图片
        image = eval(img).get(0)
        return JsonResponse(
            {'code': 200, 'msg': 'success', 'data': {'id': goods_id, 'price': price, 'title': title, 'image': image}})
