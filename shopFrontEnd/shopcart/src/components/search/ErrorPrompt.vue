<template>
  <div id="error">
    <img src="@/assets/backImage/notice.png" alt="" />
    <div class="tips">
      <span>抱歉，没有找到相关的商品</span>
      <ul>
        <li>建议您：</li>
        <li>1、适当减少筛选条件</li>
        <li>2、调整价格区间</li>
        <li>3、尝试其他关键字</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ErrorPrompt'
}
</script>

<style scoped lang="less">
#error {
  width: 1190px;
  margin: 0 auto;
  height: 205px;
  display: flex;
  justify-content: center;
  padding: 45px 0;
  border-top: 1px solid #E7E3E7;
  border-bottom: 1px solid #E7E3E7;
  img {
    width: 32px;
    height: 75px;
    padding-top: 2px;
  }
  .tips {
    text-align: left;
    ul {
      margin-bottom: 0;
      padding-left: 0;
      font-size: 12px;
    }
    span {
      font-size: 14px;
      font-weight: bold;
      color: #F60;
      line-height: 32px;
    }
  }
}
</style>
