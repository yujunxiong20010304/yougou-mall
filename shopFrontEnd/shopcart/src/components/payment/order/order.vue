<template>
<aside class="order-news">
        <h6>确认订单信息</h6>
        <div class="order-container">
            <ul class="item-headers-wrap">
                <li class="item-headers-0">店铺宝贝</li>
                <li class="item-headers-1">商品属性</li>
                <li class="item-headers-2">单价</li>
                <li class="item-headers-3">数量</li>
                <li class="item-headers-4">优惠方式</li>
                <li class="item-headers-5">小计</li>
            </ul>
            <ul style="margin: 0;padding: 0;">
              <li v-for="(item,index) in price_info" :key="index">
                <div class="order-title">
                    店铺：{{item?.shop}}
                </div>
                <div class="content-container" v-for="(value,h) in item.context" :key="value.id">
                    <ul class="info-detail">
                        <li class="item-headers-0 shop-info">
                            <img :src="value.goods_image" alt="" style="width: 50px;"/>
                            <div class="support">
                                <span>{{value.title}}</span>
                                <div>
                                    <img src="@/assets/verygoods/seven.png" alt="" />
                                    <img src="@/assets/verygoods/guarantee.png" alt="" />
                                    <img src="@/assets/verygoods/xcard.png" alt="" />
                                </div>
                            </div>
                        </li>
                        <li class="item-headers-1 shop-opt">
                          <!--<span>肉类产品【量真多，太实惠】混合80包（香辣40包+蜜汁40包）</span>
                          <span>口味:原味</span>-->
                          <span v-for="opt in value.opts" :key="opt.id">{{opt.type}}：{{opt.content}}</span>
                          <span v-if="!value.opts">无</span>
                          <span v-if="value.opts?.length<1">无</span>
                        </li>
                        <li class="item-headers-2 price">
                            {{value.price}}.00
                        </li>
                        <li class="item-headers-3 shop-number" v-if="value.num">
                          <button class="iconfont" @click="value.num++">&#xe654;</button>
                          <input v-model="value.num"
                                   type="number"
                                   autocomplete="off"
                                   @blur="sureChange"
                                   onkeypress="return (/[\d]/.test(String.fromCharCode(event.keyCode)))"
                                   style="ime-mode:Disabled">
                          <button class="iconfont" @click="reduction(index, h)">&#xe656;</button>
                        </li>
                        <li class="item-headers-3 shop-number" v-else>
                            <button class="iconfont" @click="number++">&#xe654;</button>
                            <input v-model="number"
                                   type="number"
                                   autocomplete="off"
                                   @blur="sureChange"
                                   onkeypress="return (/[\d]/.test(String.fromCharCode(event.keyCode)))"
                                   style="ime-mode:Disabled">
                            <button class="iconfont" @click="cut">&#xe656;</button>
                        </li>
                        <li class="item-headers-4 discount">
                            省77:全名疯抢
                        </li>
                        <li class="item-headers-5 total" v-if="value.num">{{value.price*value.num}}.00</li>
                        <li class="item-headers-5 total" v-else>
                          {{value.price*number}}.00
                        </li>
                    </ul>
                </div>
              </li>
            </ul>
            <div class="sure-order-container">
              <div id="check-out">
                <div class="actual-payment">
                    <span class="check-out-title">实付款：</span>
                    <span v-if="all_price"><i>¥</i>{{all_price}}.00</span>
                    <span v-else-if="price"><i>¥</i>{{price}}.00</span>
                    <span v-else><i>¥</i>{{price_info[0]?.context[0]?.price}}.00</span>
                </div>
                <div class="send-to">
                    <span class="check-out-title">寄送至：</span>
                    <span v-for="item in address_info[index]?.city_address">{{item[0]}}</span>
                    <span>{{address_info[index]?.detailed_address}}</span>
                </div>
                <div class="consignee">
                    <span class="check-out-title">收货人：</span>
                    <span>{{address_info[index]?.name}}</span>
                    <span>{{address_info[index]?.phone}}</span>
                </div>
              </div>
              <div class="submit" @click="sureOrder">提交订单</div>
            </div>
        </div>
    </aside>
</template>

<script>
import emitter from '@/utils/event'
import { ElMessageBox } from 'element-plus'
export default {
  name: 'order',
  props: ['price_info'],
  data () {
    return {
      index: 0,
      address_info: '',
      number: 1,
      price: '',
      all_price: 0,
      shop_cart: ''
    }
  },
  methods: {
    // 确认提交订单
    sureOrder () {
      // 有购物id
      if (this.price_info[0].context[0].shop_cart) {
        let idlist = ''
        let numlist = ''
        for (let i = 0; i < this.price_info.length; i++) {
          for (let j = 0; j < this.price_info[i].context.length; j++) {
            let id = this.price_info[i].context[j].shop_cart
            let num = this.price_info[i].context[j].num
            idlist += id + '.'
            numlist += num + '.'
          }
        }
        idlist = idlist.substr(0, idlist.length - 1)
        numlist = numlist.substr(0, numlist.length - 1)
        this.sureOrderEncapsulation(idlist, numlist, 1)
      } else { // 无购物id
        let priceId = this.price_info[0].context[0].id
        let num = this.number
        this.sureOrderEncapsulation(priceId, num, 0)
      }
    },
    sureOrderEncapsulation (id, num, type) {
      this.$https.post('payment/sureOrder/', {
        receivingId: this.address_info[this.index].id, // 收货地址id
        id: id, // 价格id
        num: num, // 数量
        type: type
      }).then(res => {
        if (res.data.code === 200) {
          ElMessageBox.confirm(
            '账号：hvitqu1843@sandbox.com  登录密码：111111  支付密码：111111',
            '沙箱支付',
            {
              confirmButtonText: '沙箱支付',
              cancelButtonText: '优购支付',
              type: 'info'
            }
          ).then(() => {
            // 沙箱支付
            this.SandboxPayment(res.data.data.id)
          })
            .catch(() => {
              this.$router.push({
                path: '/sure/payment',
                query: {
                  id: res.data.data.id
                }
              })
            })
        } else {
          this.$message({
            type: 'error',
            message: '在个人主页中该类商品尚未付款'
          })
        }
      }).catch(err => {
        console.log(err)
      })
    },
    cut () {
      if (this.number > 1) {
        this.number--
      }
    },
    SandboxPayment (id) {
      this.$https.post('payment/sandbox_payment/', { id: String(id) }).then(res => {
        if (res.data.code === 200) {
          window.location.href = res.data.data
        }
      }).catch(err => {
        console.log(err)
      })
    },
    reduction (index, i) {
      let num = this.price_info[parseInt(index)].context[parseInt(i)].num
      if (num > 1) {
        this.$emit('QuantityReduction', { index, i })
      }
    },
    sureChange () {
      if (!this.number) {
        this.number = 1
      }
    }
  },
  watch: {
    number: {
      handler (newValue, oldValue) {
        if (newValue) {
          this.price = newValue * this.price_info[0].context[0].price
        }
      }
    },
    price_info: {
      handler (newValue, oldValue) {
        this.all_price = 0
        if (newValue) {
          for (let i = 0; i < newValue.length; i++) {
            for (let j = 0; j < newValue[i].context.length; j++) {
              let num = newValue[i].context[j].num
              let price = newValue[i].context[j].price
              this.all_price += parseInt(num) * parseInt(price)
            }
          }
        }
      },
      deep: true
    }
  },
  mounted () {
    if (typeof this.$route.query.num !== 'string') {
      this.number = this.$route.query.num
    }
    emitter.on('foo', (e) => {
      this.index = e.aim
    })
    emitter.on('address', (e) => {
      this.address_info = e.aim
    })
  }
}
</script>

<style scoped lang="less">
.order-news {
  width: 990px;
  margin: 25px auto 0;
  h6 {
    color: #333;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 7px;
  }
}
.item-headers-wrap {
  width: 990px;
  display: flex;
  margin: 0;
  padding: 0;
  justify-content: space-between;
  li {
    text-align: center;
    border-bottom: 2px solid #B2D1FF;
  }
}
.item-headers-0 {
  width: 255px;
}
.item-headers-1 {
  width: 180px;
}
.item-headers-2 {
  width: 120px;
  text-align: center;
}
.item-headers-3 {
  width: 120px;
  text-align: center;
}
.item-headers-4 {
  width: 180px;
  text-align: center;
}
.item-headers-5 {
  width:  130px;
  text-align: center;
  overflow: hidden;
}
.order-title {
  border-bottom: 1px dotted #B2D1FF;
  margin-top: 25px;
  color: #3c3c3c;
}
.info-detail {
  width: 990px;
  display: flex;
  margin: 0;
  height: 80px;
  border-bottom: 1px dotted #DDDDDD;
  padding: 7px 0 0;
  align-items: flex-start;
  justify-content: space-between;
  background-color: #FBFCFF;
}
.support {
  display: inline-block;
  margin-left: 10px;
  span {
    width: 180px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow:ellipsis;
    display: inline-block;
  }
  div {
    img {
      margin-right: 7px;
    }
  }
}
.shop-number {
  display: flex;
  align-items: center;
  padding: 10px 0;
  justify-content: center;
  button {
    border: 1px solid #e6e7eb;
    background-color: #f7f8fa;
    font-size: 16px;
    width: 34px;
    height: 26px;
  }
  input {
    width: 34px;
    height: 26px;
    text-align: center;
    color: #333;
    outline:none;
    border: 1px solid #C4C6CF;
    border-radius: 1px;
    margin: 0 2px;
  }
}
.total {
  font-weight: bold;
  color: rgb(255, 0, 54);
  font-size: 14px;
  text-align: right;
  padding: 10px 0;
}
.shop-info {
  display: flex;
  text-align: left;
  padding: 10px 0 10px 10px;
}
.shop-opt {
  padding: 10px 0;
  overflow: hidden;
  text-align: center;
  span {
    padding-right: 10px;
  }
}
.price {
  padding: 10px 0;
}
.discount {
  padding: 10px 0;
}
.content-container {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
.sure-order-container {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
#check-out {
  height: 123px;
  border: 1px solid red;
  margin-top: 25px;
  text-align: right;
  padding: 10px 5px 10px 20px;
}
.check-out-title{
  color: #333;
  font-weight: bold;
}
.actual-payment span:last-child{
  color: rgb(255, 0, 54);
  font: 700 26px tahoma;
}
.actual-payment span:last-child i {
  margin-right: 4px;
  color: #999;
  font-size: 26px;
  font-style: normal;
  font-family: verdana,serif;
}
.send-to {
  margin-top: 7px;
  span {
    margin-right: 3px;
  }
}
.consignee {
  span {
    margin-right: 3px;
  }
}
.submit {
  width: 182px;
  height: 39px;
  color: #fff;
  background-color: rgb(255, 0, 54);
  text-align: center;
  line-height: 39px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
}

input[type="number"] {
    -moz-appearance: textfield;
}
</style>
