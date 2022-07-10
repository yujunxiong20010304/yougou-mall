<template>
  <div id="payment-heads">
    <div id="heads">
      <div id="left">
        <img src="@/assets/verygoods/payment.png" alt="" />
        <span class="cashier">我的收银台</span>
        <span class="edition">中国大陆版 <i class="iconfont">&#xe66a;</i></span>
      </div>
      <div id="right">
        <span>支付宝账户：<i>{{name}}</i></span>
        <div>
          <span>找人代付</span>｜<span>唯一热线：95188</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'heads',
  props: ['name']
}
</script>

<style scoped lang="less">
#payment-heads {
  width: 100%;
  height: 50px;
  border-bottom: 1px solid #D7D8D8;
  background-color: #fff;
}
#heads {
  width: 950px;
  height: 50px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12px;
  #left {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 315px;
    .cashier {
      border-left: 1px solid #808080;
      padding-left: 7px;
      font-size: 18px;
      font-weight: 400;
      color: #1a1a1a;
    }
    .edition {
      background-color: #EFF0F1;
      color: #5C6A6F;
      font-size: 14px;
      padding: 2px 6px;
      cursor: pointer;
    }
    img {
      width: 88px;
      height: 30px;
    }
  }
  #right {
    display: flex;
    width: 327px;
    align-items: center;
    justify-content: space-between;
    i {
      font-style: normal;
      font-weight: bold;
    }
  }
}
</style>
