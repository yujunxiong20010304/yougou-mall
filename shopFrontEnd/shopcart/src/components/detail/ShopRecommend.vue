<template>
  <div class="store-push">
    <div class="push-title">
      <span>店长推荐</span>
    </div>
    <ul id="recommend-all" v-if="recommended">
      <li class="recommend" v-for="item in recommended" :key="item.id" @click="enterDetail(item.id)">
        <div class="recommend-image">
          <img :src="item.goods_image" alt="">
          <span>{{item.title}}</span>
        </div>
        <span class="recommend-price">¥ {{item.min_price}}.00</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ShopRecommend',
  props: ['recommended'],
  methods: {
    enterDetail (id) {
      const newpage = this.$router.resolve({
        path: '/detail', // 跳转的页面路由
        query: { // 要传的参数
          id: id
        }
      })
      window.open(newpage.href, '_blank')
    }
  }
}
</script>

<style scoped lang="less">
.store-push {
  width: 1210px;
  height: 265px;
  margin: 0 auto;
  .push-title {
    width: 1210px;
    height: 38px;
    border-bottom: 1px solid #e4393c;
    background-color: #f7f7f7;
    span {
      background-color: #e4393c;
      color: #fff;
      font-size: 14px;
      width: 106px;
      height: 38px;
      display: block;
      text-align: center;
      line-height: 38px;
    }
  }
  #recommend-all {
    display: flex;
    margin: 0;
    padding: 10px 0;
    .recommend {
      margin: 10px 20px;
      width: 160px;
      height: 184px;
      cursor: pointer;
    }
  }
}
.recommend-image {
  width: 160px;
  height: 160px;
  overflow: hidden;
  position: relative;
  &:hover span{
    bottom: 0;
    transition: all .2s;
  }
  span {
    position: absolute;
    font-size: 12px;
    color: #fff;
    background: rgba(0,0,0,.7);
    bottom: -36px;
    display: -webkit-box;
    -webkit-line-clamp: 2;  /*数字是几就显示几行*/
    -webkit-box-orient: vertical;
    overflow: hidden;
    padding-left: 10px;
    width: 160px;
    height: 36px;
    transition: all .2s;
  }
  img {
    width: 160px;
    height: 160px;
  }
}

.recommend-price {
    color: #e4393c;
    font-size: 14px;
    font-family: Verdana;
    font-weight: bold;
    display: block;
    width: 160px;
    height: 19px;
    line-height: 19px;
    text-align: center;
    margin-top: 5px;
}
</style>
