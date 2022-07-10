<template>
  <div id="payment">
    <heads :name="username"></heads>
    <scan-code :store="store" :title="title" :num="num" :price="price" :number="number"></scan-code>
    <payoff :num="num" :price="price" :balance="balance"></payoff>
    <ending></ending>
  </div>
</template>

<script>
import heads from '@/components/payment/payment/heads'
import ScanCode from '@/components/payment/payment/ScanCode'
import payoff from '@/components/payment/payment/payoff'
import ending from '@/components/payment/payment/ending'
export default {
  name: 'payment',
  data () {
    return {
      store: '',
      title: '',
      price: '',
      num: '',
      number: '',
      balance: '',
      username: ''
    }
  },
  components: {
    heads: heads,
    'scan-code': ScanCode,
    payoff: payoff,
    ending: ending
  },
  methods: {
    getShopCart () {
      this.$https.post('payment/orderInfo/', { id: this.$route.query.id }).then(res => {
        if (res.data.code === 200) {
          this.username = res.data.data.result.username
          this.balance = res.data.data.result.balance
          this.num = res.data.data.result.num
          this.title = res.data.data.result.title
          this.store = res.data.data.result.store
          this.price = res.data.data.result.price
          this.number = res.data.data.result.number
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created () {
    this.getShopCart()
  }
}
</script>

<style scoped lang="less">
#payment {
  background-color: #EFF0F1;
}
</style>
