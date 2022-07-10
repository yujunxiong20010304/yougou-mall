from rest_framework.response import Response

from utils.token_verify import MyApiView  # 被修改了内部函数的APIView
from utils.data_process import shop_info, data_conversion, new_shop_category, \
    clean_image_args, new_showPrice, clean_brand, paging
from payment.models import ShoppingCart, Price
from django.db.models import Q, Count, Min, Max, Avg
from store.models import Opt, City
from django.http import JsonResponse
from store.models import Goods
import json
from django.views.decorators.http import require_POST, require_GET
from django.core.paginator import Paginator
from payment.models import Assess
from oauth.models import User


# 获取用户信息
class userInfo(MyApiView):
    @staticmethod
    def post(request):
        username = request.user.username
        user_image = request.user.head_portrait
        balance = request.user.balance
        email = request.user.email
        return Response({'code': 200,
                         'msg': 'success',
                         'data': {'username': username, 'user_image': user_image, 'balance': balance, 'email': email}},
                        status=200)


# 获取用户购物信息
class ShoppingInfo(MyApiView):
    @staticmethod
    def post(request):
        user_id = request.user.id
        status = ShoppingCart.objects.filter(user_id=user_id).values('status').annotate(num=Count('status'))
        assess = ShoppingCart.objects.filter(Q(user_id=user_id), Q(is_assess=0), Q(status=5)).count()  # 待评价
        return Response({'code': 200, 'msg': 'success', 'data': {'shop_info': shop_info(status, assess)}})


# 商品信息响应
@require_POST
def goodsInfo(request):
    data = json.loads(request.body)
    theme = data.get('theme')
    number = data.get('number')
    interval = data.get('interval')
    if not (theme and number):
        return JsonResponse({'code': 404, 'msg': 'success', 'data': ''})
    shops = Goods.objects.filter(title__contains=theme).values('id', 'score', 'store', 'title', 'goods_image').annotate(
        min_price=Min('price__price'))[0:number:interval]
    shops = data_conversion(shops)
    return JsonResponse({'code': 200, 'msg': 'success', 'data': shops})


def shopDetailInfo(request):
    data = json.loads(request.body)
    # 商品id
    goods_id = data.get('id')
    if not goods_id:
        return JsonResponse({'code': 404, 'msg': 'fail', 'data': ''})
    # 商品信息
    goods = Goods.objects.filter(id=goods_id).values().first()
    if not goods:
        return JsonResponse({'code': 404, 'msg': 'fail', 'data': ''})
    # 商品名称
    title = goods.get('title')
    # 商品配置信息
    opt = Opt.objects.filter(goods_id_id=goods_id).values('id', 'type', 'content', 'image').order_by('type')
    opt = new_shop_category(opt)
    # 商品价格区间
    price_range = Price.objects.filter(goods_id=goods_id).all().aggregate(Min('price'), Max('price'))
    # 商品展示图片
    show_images = eval(goods.get('goods_image'))
    # 店铺名称
    shop = goods.get('shop')
    # 商品文字参数
    details_args = eval(goods.get('goods_parameter'))
    # 品牌
    store = goods.get('store')
    # 店长推荐数据展示
    recommended = Goods.objects.filter(Q(shop=shop) | Q(store=store)).values('id', 'score', 'store', 'title',
                                                                             'goods_image').annotate(
        min_price=Min('price__price'))[0:6]
    recommended = data_conversion(recommended)
    if len(recommended) != 6:
        shops = Goods.objects.filter(title__contains='手机').values('id', 'score', 'store', 'title',
                                                                  'goods_image').annotate(
            min_price=Min('price__price'))[0:6 - len(recommended)]
        shops = data_conversion(shops)
        recommended = shops + recommended
    # 商品图片参数
    image_args = eval(goods.get('image_parameter'))
    image_args = clean_image_args(image_args)
    # 商品的评价数
    evaluate = Assess.objects.filter(goods_id=goods_id).count()
    return JsonResponse({'code': 200, 'msg': 'success', 'data': {
        'show_images': show_images,  # 商品用于展示的图片
        'opt': opt,  # 商品配置
        'price_range': price_range,  # 商品最高价格与最低价格
        'details_args': details_args,  # 商品文字参数
        'image_args': image_args,  # 商品图片参数
        'evaluate': evaluate,  # 商品评价数
        'title': title,  # 商品的名称,
        'shop': shop,  # 店铺名称
        'recommended': recommended,  # 店长推荐的数据
    }})


def updatePrice(request):
    data = json.loads(request.body)
    result = data.get('choices')
    price = new_showPrice(result)
    return JsonResponse({'code': 200, 'msg': 'success', 'data': price})


def getAddress(request):
    data = json.loads(request.body)
    address_id = data.get('id')
    types = data.get('type')
    print(types, address_id)
    if types:
        address = City.objects.filter(parent_id=address_id).values()
    else:
        test = City.objects.filter(id=address_id).values('parent_id')
        address = City.objects.filter(parent_id=test[0]['parent_id']).values()
    print(address)
    return JsonResponse({'code': 200, 'msg': 'success', 'data': {'address': list(address)}})


# 收藏商品或购买商品
class obtainShop(MyApiView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        user_id = request.user.id  # 用户id
        types = data.get('type')  # 判断是购买还是收藏
        number = data.get('number')  # 商品的数量
        goodsId = data.get('goodsId')  # 商品的id
        priceId = data.get('priceId')
        if not priceId:
            priceId = Price.objects.filter(goods_id=goodsId).values('id', 'number').first()
            if not priceId.get('number'):
                return JsonResponse({'code': 404, 'msg': 'success', 'data': ''})
            if types:
                ShoppingCart.objects.create(num=number, user_id_id=user_id, price_id_id=priceId.get('id'))
        else:
            shop_number = Price.objects.filter(id=priceId).values('number').first()
            if not shop_number.get('number'):
                return JsonResponse({'code': 404, 'msg': 'success', 'data': ''})
            if types:
                ShoppingCart.objects.create(num=number, user_id_id=user_id, price_id_id=priceId)
        return JsonResponse({'code': 200, 'msg': 'success', 'data': {}})


class Search(MyApiView):
    permission_classes = []  # 禁止当前进行权限认证

    def post(self, request):
        data = json.loads(request.body)
        search = data.get('search')     # 搜索的物品
        index = data.get('index')   # 第几页
        if not (search and index):
            return JsonResponse({'code': 404, 'msg': 'fail', 'data': {}})
        brand = data.get('brand')   # 品牌限制
        aim = data.get('aim')       # 根据什么排序
        price = data.get('price')   # 如果是根据价格排序，那么就判断是正序还是倒序
        sales = data.get('sales')   # 如果根据销量排序，那么判断是正序还是逆序
        shops = ''
        data_count = ''
        if brand:
            data_count = shops = Goods.objects.filter(Q(title__contains=search) & Q(store__contains=brand)).count()
        else:
            data_count = shops = Goods.objects.filter(title__contains=search).count()
        page = paging(int(data_count), int(index), 50)
        start_index = page.get('start_index')
        end_index = page.get('end_index')
        # aim=1,以价格来排序
        if aim:
            # 升序
            if price:
                if brand:
                    shops = Goods.objects. \
                        filter(Q(title__contains=search) & Q(store__contains=brand)). \
                        values('id', 'score', 'store', 'title', 'goods_image'). \
                        annotate(min_price=Min('price__price')).order_by("-min_price")[start_index:end_index]
                else:
                    shops = Goods.objects. \
                        filter(title__contains=search). \
                        values('id', 'score', 'store', 'title', 'goods_image'). \
                        annotate(min_price=Min('price__price')).order_by("-min_price")[start_index:end_index]
            # 降序
            else:
                if brand:
                    shops = Goods.objects. \
                        filter(Q(title__contains=search) & Q(store__contains=brand)). \
                        values('id', 'score', 'store', 'title', 'goods_image'). \
                        annotate(min_price=Min('price__price')).order_by("min_price")[start_index:end_index]
                else:
                    shops = Goods.objects. \
                        filter(title__contains=search). \
                        values('id', 'score', 'store', 'title', 'goods_image'). \
                        annotate(min_price=Min('price__price')).order_by("min_price")[start_index:end_index]
        # aim=0，以销量来排序
        else:
            # 升序
            if sales:
                if brand:
                    shops = Goods.objects.\
                        filter(Q(title__contains=search) & Q(store__contains=brand)).\
                        values('id','score','store','title','goods_image').\
                        annotate(min_price=Min('price__price')).order_by("-min_price")[start_index:end_index]
                else:
                    shops = Goods.objects.\
                        filter(title__contains=search).\
                        values('id', 'score', 'store', 'title','goods_image').\
                        annotate(min_price=Min('price__price')).order_by("-min_price")[start_index:end_index]
            # 降序
            else:
                if brand:
                    shops = Goods.objects. \
                        filter(Q(title__contains=search) & Q(store__contains=brand)). \
                        values('id', 'score', 'store', 'title', 'goods_image'). \
                        annotate(min_price=Min('price__price')).order_by("min_price")[start_index:end_index]
                else:
                    shops = Goods.objects. \
                        filter(title__contains=search). \
                        values('id', 'score', 'store', 'title', 'goods_image'). \
                        annotate(min_price=Min('price__price')).order_by("min_price")[start_index:end_index]
        shops = data_conversion(shops)
        if not shops:
            return JsonResponse({'code': 404, 'msg': 'success', 'data': ''})
        return JsonResponse({'code': 200, 'msg': 'success', 'data': shops, 'number': page.get('page_count', None)})


# 获取品牌
def brand(request):
    data = json.loads(request.body)
    search = data.get('search')  # 搜索的物品
    if not search:
        return JsonResponse({'code': 404, 'msg': 'fail', 'data': {}})
    brand = Goods.objects.filter(title__contains=search).values('store').distinct()
    brand = clean_brand(brand)
    if not brand:
        return JsonResponse({'code': 404, 'msg': 'fail', 'data': {}})
    return JsonResponse({'code': 200, 'msg': 'success', 'data': brand})




# 展示商品的评论信息
def show_comment(request):
    data = json.loads(request.body)
    goods_id = data.get('id')
    index = data.get('index')
    judge = data.get('judge')   # 数据筛选
    if not (goods_id and index and judge):
        return JsonResponse({'code': 404, 'msg': 'fail', 'data': {}})
    comment_all = Assess.objects.filter(goods_id=goods_id).all().count()  # 评价总数
    good_score = Assess.objects.filter(Q(goods_id=goods_id) & Q(grade__gt=3)).all().count()  # 好评数量
    medium_score = Assess.objects.filter(Q(goods_id=goods_id) & Q(grade=3)).all().count()  # 中评数量
    difference_score = Assess.objects.filter(Q(goods_id=goods_id) & Q(grade__lt=3)).all().count()  # 差评数量
    assess = None
    page_count = None
    if judge == 1:
        page = paging(comment_all,index,10)
        start_index = page.get('start_index')
        end_index = page.get('end_index')
        page_count = page.get('page_count')
        assess = Assess.objects.filter(goods_id=goods_id).order_by('create_date').all().values()[start_index:end_index]
    elif judge == 2:
        page = paging(good_score, index, 10)
        start_index = page.get('start_index')
        end_index = page.get('end_index')
        page_count = page.get('page_count')
        assess = Assess.objects.filter(Q(goods_id=goods_id)&Q(grade__gt=3)).order_by('create_date').all().values()[start_index:end_index]
    elif judge == 3:
        page = paging(medium_score, index, 10)
        start_index = page.get('start_index')
        end_index = page.get('end_index')
        page_count = page.get('page_count')
        assess = Assess.objects.filter(Q(goods_id=goods_id) & Q(grade=3)).order_by('create_date').all().values()[start_index:end_index]
    elif judge == 4:
        page = paging(difference_score, index, 10)
        start_index = page.get('start_index')
        end_index = page.get('end_index')
        page_count = page.get('page_count')
        assess = Assess.objects.filter(Q(goods_id=goods_id) & Q(grade__lt=3)).order_by('create_date').all().values()[start_index:end_index]
    result = []
    for i in assess:
        user_id = i.get('user_id_id')   # 用户id
        goods_id = i.get('goods_id_id')     # 商品id
        user = User.objects.filter(id=user_id).values('username', 'head_portrait').first()
        user.update(i)
        result.append(user)
    if not result:
        return JsonResponse({'code': 404, 'msg': 'fail', 'data': {}})
    grade_avg = Assess.objects.filter(goods_id=goods_id).aggregate(avg=Avg('grade'))
    goods_score = int(grade_avg['avg']*20)
    return JsonResponse({'code': 200, 'msg': 'success', 'data':
        {
            'result': result,
            'page_count': page_count,
            'comment_all': comment_all,
            'good_score': good_score,
            'medium_score': medium_score,
            'difference_score': difference_score,
            'goods_score': goods_score
        }
    })
