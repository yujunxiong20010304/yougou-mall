<template>
  <div id="purchase">
    <all-header></all-header>
    <heads></heads>
    <place @childClick="childClick"></place>
    <station></station>
    <order :price_info="price_info" @QuantityReduction="QuantityReduction"></order>
    <all-tail></all-tail>
  </div>
</template>

<script>
import heads from '@/components/payment/order/heads'
import place from '@/components/payment/order/place'
import station from '@/components/payment/order/station'
import order from '@/components/payment/order/order'
import emitter from '@/utils/event'
export default {
  name: 'SureOrder',
  components: {
    heads: heads,
    place: place,
    station: station,
    order: order
  },
  data () {
    return {
      price_info: ''
    }
  },
  // 需要获取的数据有用户的收货地址信息，商品图片，数量，价格，简介，图片，店铺名
  methods: {
    QuantityReduction (msg) {
      let index = msg.index
      let i = msg.i
      this.price_info[index].context[i].num--
    },
    childClick () {
      this.getStoreInfo()
    },
    getStoreInfo () {
      if (this.$route.query.type) {
        this.$https.post('payment/shop_cart_order/', { result: this.$route.query }).then(res => {
          if (res.data.code === 200) {
            this.price_info = res.data.data.result
            emitter.emit('address', { aim: res.data.data.address_info })
          }
        }).catch(err => {
          console.log(err)
        })
      } else {
        this.$https.post('payment/storeInfo/', { result: this.$route.query }).then(res => {
          if (res.data.code === 200) {
            this.price_info = res.data.data.result
            emitter.emit('address', { aim: res.data.data.address_info })
          }
        }).catch(err => {
          console.log(err)
        })
      }
    }
  },
  created () {
    this.getStoreInfo()
  }
}
</script>

<style scoped lang="less">
#purchase {
  font-size: 12px;
  text-align: left;
  // background-color: rgba(240, 240, 240, .5);
}
</style>
