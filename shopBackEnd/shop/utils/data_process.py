from payment.models import Price
from django.db.models import Q, Min
from store.models import Goods, Opt, OptName
import random
from django.core.mail import send_mail
from shop.settings import EMAIL_FROM
import re
from alipay import AliPay, AliPayConfig
from shop.settings import APP_PRIVATE_KEY, ALIPAY_PUBLIC_KEY, ALIPAY_APP_ID, RETURN_URL
import math


# 处理用户购物信息
def shop_info(status, assess):
    lists = ['购物车', '待付款', '待发货', '待收货', '待评价']
    result = [{'status': x, 'num': 0} for x in [1, 2, 3, 6]]
    for i in result:
        for j in status:
            if i['status'] == j['status']:
                i['num'] = j['num']
    result.append({'status': '待评价', 'num': assess})
    for i in range(len(lists)):
        result[i]['status'] = lists[i]
    return result


# 处理商品展示信息
def data_conversion(data):
    result = []
    for i in data:
        i['goods_image'] = eval(i.get('goods_image')).get(0)
        result.append(i)
    return result


# 处理商品的选择
def new_shop_category(opt):
    data = list(set([i['type'] for i in opt]))
    opts = []
    for i in data:
        result = OptName.objects.filter(id=i).values('name').first()
        temporary = []
        for x in opt:
            if x['type'] == i:
                str1 = re.sub('https', 'https:', x['image'])
                x['image'] = str1
                temporary.append(x)
        result['content'] = temporary
        opts.append(result)
    return opts


# 清洗商品的图片参数
def clean_image_args(image_args):
    for key in list(image_args.keys()):
        h = image_args[key].split('https:')
        h = 'https:' + h[-1]
        image_args[key] = h.split('.jpg')[0] + '.jpg'
        if image_args[key] == 'https://gfs1.gomein.net.cn/T1i0xSBXWT1RCvBVdK.jpg':
            del image_args[key]
            continue
        if len(image_args[key]) < 20:
            del image_args[key]
    return image_args


def new_showPrice(result):
    ids = list(result.values())
    ids = sorted(ids)
    if len(ids) <= 1:
        for i in range(5 - len(ids)):
            ids.append(None)
    else:
        for i in range(5 - len(ids)):
            ids.append(0)
    price = Price.objects.filter(
        Q(typeZero=ids[0]) & Q(typeOne=ids[1]) & Q(typeTwo=ids[2]) & Q(typeThree=ids[3]) & Q(typeFour=ids[4])).values(
        'price', 'id').first()
    return price


# 发送邮箱验证码
def sendMessage(email):
    code_string = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    codes = list(code_string)
    data = "".join(random.sample(codes, 6))
    message = "您的验证码是" + data + "，10分钟内有效，请尽快填写"
    send_mail('优购', message, EMAIL_FROM, [email], fail_silently=False)
    return data


# 从立即购买到订单确定的商品配置的文字展示
def text_description_configure(priceId):
    opt_info = Price.objects.filter(id=priceId).values('typeZero', 'typeOne', 'typeTwo', 'typeThree',
                                                       'typeFour').first()
    opts = list(opt_info.values())
    data = []
    for i in opts:
        opt = Opt.objects.filter(id=i).first()
        result = {}
        if opt:
            result['content'] = opt.content
            result['type'] = opt.type.name
            data.append(result)
    return data


def clean_brand(brands):
    result = []
    for i in brands:
        brand = i['store'].split('(')[0]
        result.append(brand)
    return result


def create_alipay():
    alipay = AliPay(appid=ALIPAY_APP_ID,
                    app_notify_url=None,  # 默认回调 url
                    app_private_key_string=APP_PRIVATE_KEY,  # 你的私钥
                    alipay_public_key_string=ALIPAY_PUBLIC_KEY,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
                    sign_type="RSA2",  # RSA 或者 RSA2
                    debug=False,  # 默认 False
                    verbose=False,  # 输出调试数据
                    config=AliPayConfig(timeout=15)  # 可选，请求超时时间
                    )
    # 可选，请求超时时间
    return alipay


def alipay_pay(subject, total_amount, out_trade_no, return_url_view):
    alipay = create_alipay()
    return_url = RETURN_URL + return_url_view
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=out_trade_no,
        total_amount=total_amount,
        subject=subject,
        return_url=return_url,
        notify_url="https://example.com/notify"  # 可选，不填则使用默认 notify url
    )
    return order_string


# total 查询到的总数
# index 当前所需页数
# number 需要的数量
def paging(total, index, number):
    page_count = math.ceil(total/number)    # 总页数
    if index == page_count:
        end_index = total
    else:
        end_index = index * number
    start_index = (index-1) * number
    return {'page_count': page_count, 'start_index': start_index, 'end_index': end_index}

