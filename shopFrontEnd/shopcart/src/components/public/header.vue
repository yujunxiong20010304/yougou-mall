<template>
  <div id="main">
    <div id="content">
      <span class="address"><i class="iconfont icon">&#xe6ad;</i>四川省</span>
      <ul class="choices">
        <li v-if="username"><router-link :to="{name: 'user'}">{{username}}</router-link></li>
        <li v-else><router-link :to="{name: 'Login'}">请登录</router-link></li>
        <li><router-link :to="{name: 'Register'}">注册</router-link></li>
        <li><img src="@/assets/backImage/gift_big.gif" alt="">签到有礼</li>
        <li><router-link :to="{name: 'payoff'}">我的订单</router-link></li>
        <li>我的特卖</li>
        <li>客户服务</li>
        <li>更多</li>
      </ul>
    </div>
  </div>
</template>
<script>
import jwtDecode from 'jwt-decode'
export default {
  name: 'headers',
  data () {
    return {
      username: ''
    }
  },
  // http://pv.sohu.com/cityjson?ie=utf-8
  // 在这里进行页面初始化的数据请求
  created () {
    try {
      const decode = jwtDecode(this.$store.state.token)
      this.username = decode.username
    } catch (e) {

    }
  }
}
</script>

<style scoped lang="less">
#main {
  width: 100%;
  height: 30px;
  background-color: #fff;
  font-size: 12px;
  box-shadow:0 15px 35px rgba(0,0,0,0.05),0 3px 10px rgba(0,0,0,0.05);
  .icon {
    color: red;
    font-size: 14px;
    margin-right: 2px;
  }
  #content {
    min-width: 1170px;
    max-width: 1170px;
    height: 30px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #333;
  }
  .choices {
    width: 771px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #666;
    margin: 0;
    padding: 0;
    li {
      height: 30px;
      padding: 0 30px;
      line-height: 30px;
      cursor: pointer;
      position: relative;
      a {
        color: #666;
        text-decoration: none;
      }
      img {
        position: relative;
        top: -4px;
        margin-right: 5px;
      }
      &:hover {
        color: #409EFF;
      }
      &:hover a{
        color: #409EFF;
      }
      &:after {
        content: '/';
        position: absolute;
        right: 0;
        color: #d8d8d8;
      }
    }
  }
}
</style>
