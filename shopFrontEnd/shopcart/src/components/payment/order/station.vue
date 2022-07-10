<template>
  <section class="wrapped">
    <div>
        <span>菜鸟驿站代收服务<i>免费</i></span>
    </div>
    <div>
        <i class="iconfont">&#xe682;</i>收货不便，可以使用<a href="javascript:">菜鸟驿站代收服务</a>
    </div>
  </section>
</template>

<script>
export default {
  name: 'station'
}
</script>

<style scoped lang="less">
.wrapped {
  width: 990px;
  height: 82px;
  border: 2px solid #EEEEEE;
  margin: 14px auto;
  div {
    &:first-child {
      height: 25px;
      border-bottom: 1px solid #DCDEE3;
    }
    &:last-child {
      width: 100%;
      height: 54px;
      padding: 15px 5px 5px 15px;
      display: flex;
      align-items: center;
      i {
        color: red;
        font-size: 20px;
        margin-right: 5px;
      }
      a {
        color: #CC9977;
        text-decoration: none;
        margin-left: 5px;
      }
    }
    span {
      color: #666;
      border-top: 2px solid red;
      display: inline-block;
      height: 25px;
      line-height: 25px;
      padding: 0 15px;
      border-bottom: 1px solid white;
      i {
        padding: 1px 5px;
        background-color: red;
        color: #fff;
        border-radius: 2px;
        margin-left: 10px;
        font-style: normal;
      }
    }
  }
}
</style>
