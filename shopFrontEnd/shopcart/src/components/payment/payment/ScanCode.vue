<template>
  <div id="scan-code">
    <div id="left">
      <img src="@/assets/verygoods/pay.png" alt="" />
      <div v-if="num">
        <span>优购YouGou -- {{title}}</span>
        <span>卖家昵称：{{ store }}</span>
      </div>
      <div v-else>
        <span>合并｜{{number}}笔订单</span>
      </div>
    </div>
    <div id="right">
      <div>
        <span v-if="num">{{parseInt(num)*parseInt(price)}}.00</span>
        <span v-else>{{price}}.00</span>
        <i>元</i>
      </div>
      <a href="javascript:void(0)">订单详情</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ScanCode',
  props: ['store', 'title', 'num', 'price', 'number']
}
</script>

<style scoped lang="less">
#scan-code {
  width: 950px;
  height: 125px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 4px solid #B3B3B3;
  img {
    width: 100px;
    height: 100px;
  }
  #left {
    display: flex;
    align-items: center;
    height: 100%;
    width: 80%;
    div {
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      text-align: left;
      font-size: 12px;
      padding-left: 25px;
      font-weight: 500;
      height: 54px;
    }
  }
  #right {
    margin-right: 25px;
    position: relative;
    height: 121px;
    line-height: 121px;
    span {
      font-size: 22px;
      font-weight: bold;
      color: #FF8206;
      font-family: tahoma,serif;
    }
    i {
      padding-left: 5px;
      font-size: 12px;
      color: #3D3D3D;
      font-style: normal;
    }
    a {
      font-size: 12px;
      text-decoration: none;
      position: absolute;
      bottom: -4px;
      left: 50%;
      transform: translate(-50%, 0);
      width: 64px;
      background-color: #B3B3B3;
      color: #fff;
      display: inline-block;
      height: 22px;
      line-height: 22px;
      &:hover {
        text-decoration: underline;
      }
    }
  }
}
</style>
