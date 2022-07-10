<template>
  <div id="pack-list">
    <em>包装清单</em>
    <span>【流沙台灯+遥控】【礼盒装】</span>
  </div>
</template>

<script>
export default {
  name: 'packing'
}
</script>

<style scoped lang="less">
#pack-list {
  width: 990px;
  height: 69px;
  margin: 10px 0;
  color: #999;
  font-size: 12px;
  font-family: tahoma, arial, Microsoft, YaHei, Hiragino, Sans, GB, "\u5b8b\u4f53", sans-serif;
  align-items: center;
  display: none;
  text-align: left;
  em {
    font-style: normal;
    display: inline-block;
    width: 130px;
    height: 27px;
    line-height: 27px;
    text-align: right;
    margin-right: 15px;
  }
}
</style>
