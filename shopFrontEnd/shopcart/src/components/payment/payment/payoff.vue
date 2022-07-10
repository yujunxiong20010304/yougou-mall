<template>
  <div id="payoff">
    <ul>
      <li>
        <label>
          <div class="pay-mode">
            <div class="left">
              <input type="radio" alt="" name="card"/>
              <img src="@/assets/verygoods/bank.png" alt=""/>
              <span style="font-size: 14px;">四川省农村信用社联合社</span>
              <span>**2034</span>
              <span>储蓄卡 | 快捷</span>
            </div>
            <div class="right">
              <span>支付</span>
              <i v-if="num">{{parseInt(num)*parseInt(price)}}.00</i>
              <i v-else>{{price}}.00</i>
              <span>元</span>
            </div>
          </div>
        </label>
      </li>
      <li class="special">
        <label>
          <div class="pay-mode">
            <div class="left">
              <input type="radio" alt="" name="card"/>
              <img src="@/assets/verygoods/bank.png" alt=""/>
              <span style="font-size: 14px;">四川省农村信用社联合社</span>
              <span>**2034</span>
              <span>储蓄卡 | 快捷</span>
            </div>
            <div class="right">
              <span>支付</span>
              <i v-if="num">{{parseInt(num)*parseInt(price)}}.00</i>
              <i v-else>{{price}}.00</i>
              <span>元</span>
            </div>
          </div>
        </label>
      </li>
    </ul>
    <div class="pay-choice">
      <div class="add-payment">添加快捷/网银付款</div>
      <div class="add-payment other">其他付款方式</div>
    </div>
    <div class="pay-code">
      <span>支付宝支付密码:</span>
      <el-input v-model="password" type="password" placeholder="" show-password/>
      <el-button type="primary" class="sure" @click="SurePayment">确认付款</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'payoff',
  props: ['num', 'price', 'balance', 'id'],
  data () {
    return {
      password: ''
    }
  },
  methods: {
    SurePayment () {
      this.$https.post('payment/surePayment/',
        { id: this.$route.query.id, password: this.$jsEncrypt(this.password, this.$store.state.publicKey) }
      ).then(res => {
        if (res.data.code === 200) {
          this.$router.replace({
            path: '/home'
          })
        } else {
          this.$message({
            type: 'error',
            message: res.data.msg
          })
        }
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped lang="less">
#payoff {
  width: 950px;
  background-color: white;
  margin: 0 auto;
  padding: 20px;
  border-bottom: 4px solid #A6A6A6;
  ul {
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    li {
      margin-bottom: 7px;
    }
  }
  .pay-mode {
    width: 910px;
    height: 60px;
    padding: 0 25px;
    border: 4px solid #85a1d4;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    .left {
      display: flex;
      align-items: center;
      font-size: 12px;
      width: 357px;
      justify-content: space-between;
    }
    .right {
      display: flex;
      align-items: center;
      font-size: 12px;
      i {
        font-style: normal;
        font-size: 16px;
        color: #ff8208;
        font-weight: 700;
        font-family: tahoma,serif;
        padding: 0 5px;
      }
    }
  }
  .special {
    .pay-mode {
      border: 4px solid #85a1d4;
    }
    border-bottom: 1px solid #ccc;
  }

  .pay-choice {
    display: flex;
    width: 100%;
    .add-payment {
      width: 135px;
      height: 33px;
      border: 1px dashed #ccc;
      text-align: center;
      line-height: 33px;
      font-size: 12px;
      color: #16AEEF;
      cursor: pointer;
      margin-top: 10px;
      &:hover {
        background-color: #0087CC;
        color: #fff;
        border: 1px solid #ccc;
      }
    }
    .other {
      border: 1px solid #ccc;
      margin-left: 20px;
    }
  }

  .pay-code {
    width: 600px;
    display: flex;
    flex-direction: column;
    margin-top: 25px;
    height: 111px;
    span {
      text-align: left;
      font-size: 14px;
      color: #333;
    }
    :deep(.el-input) {
      width: 295px;
      height: 32px;
      margin-top: 5px;
    }
    .sure {
      width: 85px;
      margin-top: 20px;
    }
  }
}
</style>
