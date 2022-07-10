import random
import string
from utils.token_verify import MyApiView  # 被修改了内部函数的APIView
from utils.data_process import text_description_configure, create_alipay, alipay_pay
from django.http import JsonResponse
import json
from payment.models import ShoppingCart, Price, Receiving
from store.models import Goods
from django.db.models import Q
from shop.settings import GATEWAY
from shop.settings import pri_key, pub_key
from utils.rsa_crypt import decrypt_data


# 用户点击购买后的商品以及收货地址信息的展示
class StoreInfo(MyApiView):
    @staticmethod
    def post(request):
        user_id = request.user.id  # 用户id
        data = json.loads(request.body).get('result')  # 前端传输来的数据
        priceId = data.get('priceId', None)  # 商品的价格id
        shopId = data.get('id')  # 商品id

        # 说明该商品没有配置信息
        if not priceId:
            price_info = Price.objects.filter(goods_id=shopId).values('id', 'price', 'goods_id').first()
            goods_info = Goods.objects.filter(id=shopId).values('shop', 'store', 'title', 'goods_image').first()
            price_info.update(goods_info)
        else:
            price_info = Price.objects.filter(id=priceId).values('id', 'price', 'goods_id').first()
            goods_info = Goods.objects.filter(id=shopId).values('shop', 'store', 'title', 'goods_image').first()
            price_info.update(goods_info)
            # 配置的文字描述信息
            opt_info = text_description_configure(priceId)
            price_info['opts'] = opt_info
        price_info['goods_image'] = eval(price_info.get('goods_image')).get(0)
        result = {'shop': price_info['shop'], 'context': [price_info]}
        # 收货地址信息
        address_info = Receiving.objects.filter(Q(user_id=user_id) & Q(state=1)).values('id', 'name', 'phone',
                                                                                        'city_address',
                                                                                        'detailed_address')
        for i in address_info:
            i['city_address'] = eval(i.get('city_address'))
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {
            'address_info': list(address_info),
            'result': [result]
        }})


# 添加新的收货地址
class AddUserAddress(MyApiView):
    @staticmethod
    def post(request):
        user_id = request.user.id  # 用户id
        data = json.loads(request.body)
        address_id = data.get('id')
        city_address = data.get('address')  # 地址列表
        detailed_address = data.get('explicit_address')  # 详细地址
        phone = data.get('phone')  # 电话号码
        postal_code = data.get('postal_code')  # 邮箱编号
        if not postal_code:
            postal_code = '000000'
        name = data.get('receiving')  # 收货人姓名
        if not address_id:
            Receiving.objects.create(name=name,
                                     user_id_id=user_id,
                                     city_address=str(city_address),
                                     detailed_address=detailed_address,
                                     phone=phone,
                                     postal_code=postal_code)
        else:
            Receiving.objects.filter(id=address_id).update(name=name,
                                                           user_id_id=user_id,
                                                           city_address=str(city_address),
                                                           detailed_address=detailed_address,
                                                           phone=phone,
                                                           postal_code=postal_code)
        address_info = Receiving.objects.filter(Q(user_id=user_id) & Q(state=1)).values('id', 'name', 'phone',
                                                                                        'city_address',
                                                                                        'postal_code',
                                                                                        'detailed_address')
        for i in address_info:
            i['city_address'] = eval(i.get('city_address'))
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {'address_info': list(address_info)}})


# 确认订单
class SureOrder(MyApiView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        user_id = request.user.id
        id = data.get('id')  # 商品的id或者说是价格id
        num = data.get('num')  # 数量
        types = data.get('type')  # 前端传输的数据类型
        receiving_id = data.get('receivingId')
        if types:  # 对数据库中购物车表商品状态进行修改
            ids = id.split('.')
            nums = num.split('.')
            for index in range(len(ids)):
                ShoppingCart.objects.filter(id=ids[index]).update(status=2, num=nums[index], receiving=receiving_id)
            return JsonResponse({'code': 200, 'msg': 'success', 'data': {'id': id}})
        else:
            # 判断待付款中是否已有该商品存在
            existence = ShoppingCart.objects.filter(Q(user_id=user_id) & Q(status=2) & Q(price_id=id)).count()
            if existence:
                return JsonResponse({'code': 404, 'msg': 'fail', 'data': ''})
            shop_cart = ShoppingCart.objects.create(receiving=receiving_id, num=num, status=2, price_id_id=id,
                                                    user_id_id=user_id)
            return JsonResponse({'code': 200, 'msg': 'success', 'data': {'id': shop_cart.id}})


class OrderInfo(MyApiView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        id = data.get('id').split('.')
        username = request.user.username
        balance = request.user.balance
        # 需要查询出来的内容
        # 购物车的id，数量，价格，用户的余额，用户民，商品的标题，商店名
        if len(id) > 1:
            price = 0
            for i in id:
                shop_cart = ShoppingCart.objects.filter(id=i).first()
                price += shop_cart.price_id.price * shop_cart.num
            order_info = {'username': username, 'balance': balance, 'price': price, 'number': len(id)}
            return JsonResponse({'code': 200, 'msg': 'success', 'data': {'result': order_info}})
        else:
            shop_cart = ShoppingCart.objects.filter(id=id[0]).values('price_id', 'num', 'id').first()
            price_id = shop_cart.get('price_id')
            price = Price.objects.filter(id=price_id).first()
            title = price.goods_id.title
            store = price.goods_id.store
            order_info = {'username': username, 'balance': balance, 'price': price.price, 'title': title,
                          'store': store}
            order_info.update(shop_cart)
            return JsonResponse({'code': 200, 'msg': 'success', 'data': {'result': order_info}})


# 沙箱支付
class SandboxPayment(MyApiView):
    def post(self, request):
        data = json.loads(request.body)
        id_str = data.get('id')
        id = data.get('id').split('.')  # 购物车id/可能是多个
        username = request.user.username
        balance = request.user.balance
        total_amount = ''
        subject = ''
        if len(id) > 1:
            total_amount = 0
            for i in id:
                shop_cart = ShoppingCart.objects.filter(id=i).first()
                total_amount += shop_cart.price_id.price * shop_cart.num
                subject = '合计{}笔订单'.format(len(id))
        else:
            shop_cart = ShoppingCart.objects.filter(id=id[0]).values('price_id', 'num', 'id').first()
            price_id = shop_cart.get('price_id')
            num = shop_cart.get('num')  # 数量
            price = Price.objects.filter(id=price_id).first()
            total_amount = int(num) * int(price.price)  # 价格
            subject = price.goods_id.title  # 商品名称
        # print(total_amount, subject)
        out_trade_no = "".join(random.sample(string.ascii_letters + string.digits, 32)) + '/' + id_str
        order_string = alipay_pay(subject=subject, total_amount=str(total_amount), out_trade_no=out_trade_no,
                                  return_url_view='success')
        return JsonResponse({'code': 200, 'msg': 'success', 'data': GATEWAY + order_string})


# 检验支付回调
def alipay_return(request):
    data = json.loads(request.body)
    data = data.get('data')
    if not data:
        return JsonResponse({'code': 200, 'msg': 'success', 'data': ''})
    processed_dict = {}
    # 回调时alipay会把一些公用信息通过GET方式传参回来，这里用字典去接收存储
    for key, value in data.items():
        processed_dict[key] = value
    sign = processed_dict.pop("sign", None)
    new_alipay = create_alipay()
    verify_re = new_alipay.verify(processed_dict, sign)
    if verify_re is True:
        shop_cart = data.get('out_trade_no').split('/')[1].split('.')
        for i in shop_cart:
            ShoppingCart.objects.filter(id=i).update(status=3)
    else:
        print("支付失败")
        return JsonResponse({'code': 404, 'msg': 'success', 'data': ''})
    return JsonResponse({'code': 200, 'msg': 'success', 'data': ''})


class SurePayment(MyApiView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        user_id = request.user.id
        payPassword = request.user.payPassword  # 支付密码
        id = data.get('id')
        password = data.get('password')
        if not (id and password and user_id):
            return JsonResponse({'code': 404, 'msg': '缺少关键参数', 'data': {}})
        password = decrypt_data(password, pri_key)
        print(password)
        if password != payPassword:
            return JsonResponse({'code': 404, 'msg': '支付密码错误', 'data': {}})
        ids = id.split('.')
        for i in ids:
            while True:
                shop_cart = ShoppingCart.objects.filter(Q(id=i) & Q(user_id=user_id)).first()
                # 原始库存
                number = Price.objects.filter(id=shop_cart.price_id.id).values('number').first()['number']
                # 当前购买商品的数量
                num = shop_cart.num
                if number < num:
                    return JsonResponse({'code': 404, 'msg': '库存不足', 'data': {}})
                # result = ShoppingCart.objects.filter(id=i, price_id__number=number).update(status=3, price=number-num)
                result = Price.objects.filter(id=shop_cart.price_id.id, number=number).update(number=number-num)
                if result == 0:
                    continue
                else:
                    ShoppingCart.objects.filter(id=i, user_id=user_id).update(status=3)
                break
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {}})


# 地址真伪性验证
class ValidateAddress(MyApiView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        id = data.get('id')
        state = Receiving.objects.filter(id=id).values('state').first().get('state')
        if not state:
            return JsonResponse({'code': 404, 'msg': 'success', 'data': {}})
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {}})


# 从购物车跳转过来的购物
class ShopCartOrder(MyApiView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        user_id = request.user.id  # 用户id
        ids = data.get('result')['id'].split('.')  # 商品的id
        nums = data.get('result')['num'].split('.')  # 数量
        result = []
        for index in range(len(ids)):
            shop_cart = ShoppingCart.objects.filter(id=ids[index]).values('price_id').first()
            price = Price.objects.filter(id=shop_cart.get('price_id')).values('price', 'goods_id').first()
            goods = Goods.objects.filter(id=price['goods_id']).values('shop', 'store', 'title',
                                                                      'goods_image').first()  # 商品信息
            goods['goods_image'] = eval(goods['goods_image'])[0]
            goods['price'] = price.get('price')  # 价格
            goods['num'] = nums[index]
            goods['shop_cart'] = ids[index]
            goods['goods_id'] = price['goods_id']
            goods['id'] = shop_cart['price_id']
            opt_info = text_description_configure(shop_cart.get('price_id'))
            goods['opts'] = opt_info
            price_info = {'shop': goods['shop'], 'context': [goods]}
            if not result:
                result.append(price_info)
            else:
                judge = True
                for i in result:
                    if i['shop'] == price_info['shop']:
                        i['context'].append(price_info['context'][0])
                        judge = False
                if judge:
                    result.append(price_info)
        # 收货地址信息
        address_info = Receiving.objects.filter(Q(user_id=user_id) & Q(state=1)).values('id', 'name', 'phone',
                                                                                        'city_address',
                                                                                        'detailed_address')
        for i in address_info:
            i['city_address'] = eval(i.get('city_address'))
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {
            'address_info': list(address_info),
            'result': result
        }})
