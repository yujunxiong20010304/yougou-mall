<template>
  <div id="success">
    <all-header></all-header>
    <all-search></all-search>
    <div class="content">
      <img src="@/assets/backImage/success.png" alt="成功" />
      <div>
        <span class="info">订单支付成功</span>
        <span>您的订单已成功支付，支付交易号：{{order_number}}</span>
        <router-link :to="{name: 'delivery'}">您可以在【用户中心】->【待发货】查看该订单</router-link>
      </div>
    </div>
    <all-tail></all-tail>
  </div>
</template>

<script>
export default {
  name: 'success',
  data () {
    return {
      order_number: this.$route.query.out_trade_no
    }
  },
  methods: {
    alipay_return () {
      this.$https.post('payment/alipay_return/', { data: this.$route.query }).then(res => {
        console.log(res)
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created () {
    this.alipay_return()
  }
}
</script>

<style scoped lang="less">
.content{
  width: 1200px;
  height: 135px;
  border: 1px solid #DDDDDD;
  border-top: 2px solid #e3101e;
  margin: 0 auto 55px;
  display: flex;
  align-items: center;
  padding: 0 45px;
  img {
    width: 69px;
    height: 69px;
  }
  div{
    display: flex;
    flex-direction: column;
    text-align: left;
    padding-left: 25px;
    color: #666;
    font-size: 12px;
    height: 65px;
    justify-content: space-between;
    .info {
      font-weight: bold;
    }
    a {
      color: #FF8802;
      text-decoration: none;
      &:hover {
        text-decoration: underline;
      }
    }
  }
}
</style>
