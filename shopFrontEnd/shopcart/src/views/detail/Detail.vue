<template>
  <div id="detail">
    <all-header></all-header>
    <all-search></all-search>
    <shop-title></shop-title>
    <div id="shop-info">
      <shop-left :show_images="goods_detail.show_images"></shop-left>
      <shop-center
        :opt="goods_detail.opt"
        :title="goods_detail.title"
        :price_range="goods_detail.price_range"
        :evaluate="goods_detail.evaluate"
        :shop="goods_detail.shop"
      >
      </shop-center>
      <shop-right></shop-right>
    </div>
    <shop-recommend :recommended="goods_detail.recommended"></shop-recommend>
    <div id="introduce">
      <shop-introduce :recommended="goods_detail.recommended" :shop="goods_detail.shop"></shop-introduce>
      <div id="suggest">
        <div class="detail-title">
          <ul>
            <li @click="changeDisplay(1)" :class="[1 === aim?'title-select':'']">商品介绍</li>
            <li @click="changeDisplay(2)" :class="[2 === aim?'title-select':'']">规格与包装</li>
            <li @click="changeDisplay(3)" :class="[3 === aim?'title-select':'']">售后保障</li>
            <li @click="changeDisplay(4)" :class="[4 === aim?'title-select':'']">商品评价(1000+)</li>
            <li @click="changeDisplay(5)" :class="[5 === aim?'title-select':'']">类似好评商品</li>
          </ul>
          <span>加入购物车</span>
        </div>
        <shop-parameter :style="[1 < aim?'display:none':'display:block']" :details_args="goods_detail.details_args"></shop-parameter>
        <packing :style="[2 === aim?'display:flex':'display:none']"></packing>
        <image-parameter :style="[1 < aim?'display:none':'display:block']" :image_args="goods_detail.image_args"></image-parameter>
        <guarantee :style="[3 < aim?'display:none':'display:block']"></guarantee>
        <discuss :style="[4 < aim?'display:none':'display:block']"></discuss>
        <similar></similar>
      </div>
    </div>
    <all-tail></all-tail>
    <el-backtop :bottom="100" :right="15">
      <img src="@/assets/backImage/rocket.png" alt="" style="height: 100%;width: 100%;"/>
    </el-backtop>
  </div>
</template>

<script>
import titles from '@/components/detail/titles'
import ShopLeft from '@/components/detail/ShopLeft'
import ShopCenter from '@/components/detail/ShopCenter'
import ShopRight from '@/components/detail/ShopRight'
import ShopRecommend from '@/components/detail/ShopRecommend'
import ShopIntroduce from '@/components/detail/ShopIntroduce'
import ShopParameter from '@/components/detail/ShopParameter'
import ImageParameter from '@/components/detail/ImageParameter'
import packing from '@/components/detail/packing'
import guarantee from '@/components/detail/guarantee'
import discuss from '@/components/detail/discuss'
import similar from '@/components/detail/similar'
export default {
  name: 'Detail',
  components: {
    'shop-title': titles,
    'shop-left': ShopLeft,
    'shop-center': ShopCenter,
    'shop-right': ShopRight,
    'shop-recommend': ShopRecommend,
    'shop-introduce': ShopIntroduce,
    'shop-parameter': ShopParameter,
    'image-parameter': ImageParameter,
    packing: packing,
    guarantee: guarantee,
    discuss: discuss,
    similar: similar
  },
  data () {
    return {
      goods_detail: {},
      aim: 1
    }
  },
  methods: {
    changeDisplay (value) {
      this.aim = value
    },
    async goodsDetailInfo () {
      const { data: res } = await this.$http.post('store/detail/', { id: this.$route.query.id })
      if (res.code === 200) {
        this.goods_detail = res.data
      } else {
        this.$router.push({
          path: '/home'
        })
      }
    }
  },
  created () {
    this.goodsDetailInfo()
  }
}
</script>

<style scoped lang="less">
#shop-info {
  display: flex;
  width: 1246px;
  justify-content: space-between;
  margin: 25px auto 35px;
}
#introduce {
  display: flex;
  width: 1210px;
  margin: 0 auto;
  justify-content: space-between;
}
#suggest {
  width: 988px;
}
.detail-title {
  width: 988px;
  height: 38px;
  border-bottom: 1px solid #e4393c;
  background-color: #F7F7F7;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 5px;
  span {
    width: 92px;
    height: 25px;
    background-color: #DF3133;
    font-size: 14px;
    color: #fff;
    text-align: center;
    line-height: 25px;
    margin-right: 15px;
    cursor: pointer;
  }
  ul {
    display: flex;
    color: #fff;
    font-size: 14px;
    font-family: "microsoft yahei";
    padding: 0;
    margin: 0;
    height: 100%;
    li {
      padding: 10px 25px;
      margin-right: 2px;
      cursor: pointer;
      font-size: 14px;
      color: #666;
    }
    .title-select {
      background-color: #e4393c;
      color: #fff;
    }
  }
}
:deep(.el-backtop) {
  box-shadow: none;
  &:hover {
    background-color: rgba(255, 255, 255, .1);
  }
}
</style>
