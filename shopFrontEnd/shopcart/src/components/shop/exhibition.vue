<template>
  <div id="shop" to="/detail">
    <img :src="data.goods_image" alt="" />
    <span class="detail">{{data.title}}</span>
    <span class="price">¥<strong>{{data.min_price}}</strong>.00</span>
    <div id="mask">
      <span class="iconfont">&#xeb6a;</span>
      <div class="seek">
        <div><i class="iconfont">&#xe675;</i>找相似</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'exhibition',
  props: ['data']
}
</script>

<style scoped lang="less">
#shop {
  width: 190px;
  height: 266px;
  background-color: #fff;
  cursor: pointer;
  position: relative;
  box-shadow:0 15px 35px rgba(255,255,255,0.2),0 2px 5px rgba(0,0,0,0.2);
  transition: all .4s;
  margin: 5px 1px;
  img {
    width: 120px;
    height: 120px;
    margin: 30px 35px;
  }
  .detail {
    width: 170px;
    height: 40px;
    word-break: break-all;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    font-size: 12px;
    line-height: 20px;
    height: 40px;
    margin: 0 auto;
    text-align: left;
  }
  .price {
    padding-top: 7px;
    color: #e1251b;
    font-size: 12px;
    font-family: arial,sans-serif;
    font-weight: 700;
    display: inline-block;
    width: 170px;
    text-align: left;
    margin: 0 auto;
    strong {
      font-size: 16px;
    }
  }
  &:hover #mask{
    display: block;
    opacity: 1;
  }
  &:hover {
    transform: translate(0, -5px);
  }
  #mask {
    opacity: 0;
    transition: all .5s;
    position: absolute;
    width: 190px;
    height: 266px;
    top: 0;
    background: linear-gradient(180deg,rgba(255,255,255,.2) 0,rgba(255,255,255,.2) 35%,rgba(255,255,255,.2));
    span {
      position: absolute;
      right: 5px;
      color: #A7A7A7;
      font-size: 12px;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      line-height: 20px;
      text-align: center;
      top: 5px;
      &:hover {
        color: black;
      }
    }
    .seek {
      width: 100%;
      height: 62px;
      background: -webkit-gradient(linear,left top,left bottom,
      from(rgba(255,255,255,.8)),color-stop(35%,white),to(white));
      transition: all 3s;
      position: absolute;
      bottom: 0;
      div {
        position: absolute;
        bottom: 21px;
        left: 50%;
        transform: translate(-50%, 0);
        width: 99px;
        height: 28px;
        border-radius: 14px;
        background-color: #323232;
        color: #fff;
        font-size: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        .iconfont {
          font-size: 14px;
          margin-right: 4px;
        }
        &:hover {
          background-color: #C81B23;
        }
      }
    }
  }
}
</style>
