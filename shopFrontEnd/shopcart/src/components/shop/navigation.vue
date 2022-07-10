<template>
<!-- 导航 -->
  <article id="side_nav">
        <!--侧边导航栏-->
        <div id="bulletin_board">
            <ul>
                <li>
                    <i class="font h iconfont">&#xe60f;</i>
                    <!--<a href="javascript:" class="h">女装</a>-->
                    <router-link :to='{name: "Search", query:{search:"女装",rule:1,price:0,sales:0,index:1}}' class="h">女装</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"内衣",rule:1,price:0,sales:0,index:1}}' class="h">内衣</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"家居",rule:1,price:0,sales:0,index:1}}' class="h">家居</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe608;</i>
                    <router-link :to='{name: "Search", query:{search:"女鞋",rule:1,price:0,sales:0,index:1}}' class="h">女鞋</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"男鞋",rule:1,price:0,sales:0,index:1}}' class="h">男鞋</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"箱包",rule:1,price:0,sales:0,index:1}}' class="h">箱包</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe638;</i>
                    <router-link :to='{name: "Search", query:{search:"母婴",rule:1,price:0,sales:0,index:1}}' class="h">母婴</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"童装",rule:1,price:0,sales:0,index:1}}' class="h">童装</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"玩具",rule:1,price:0,sales:0,index:1}}' class="h">玩具</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe7b5;</i>
                    <router-link :to='{name: "Search", query:{search:"男装",rule:1,price:0,sales:0,index:1}}' class="h">男装</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"运动户外",rule:1,price:0,sales:0,index:1}}' class="h">运动户外</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe62f;</i>
                    <router-link :to='{name: "Search", query:{search:"美装",rule:1,price:0,sales:0,index:1}}' class="h">美装</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"彩装",rule:1,price:0,sales:0,index:1}}' class="h">彩装</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"个护",rule:1,price:0,sales:0,index:1}}' class="h">个护</router-link>
                </li>
                <li><i class="font iconfont h">&#xe6c7;</i>
                    <router-link :to='{name: "Search", query:{search:"手机",rule:1,price:0,sales:0,index:1}}' class="h">手机</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"数码",rule:1,price:0,sales:0,index:1}}' class="h">数码</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"企业",rule:1,price:0,sales:0,index:1}}' class="h">企业</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe614;</i>
                    <router-link :to='{name: "Search", query:{search:"冰箱",rule:1,price:0,sales:0,index:1}}' class="h">大家电</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"洗衣机",rule:1,price:0,sales:0,index:1}}' class="h">生活电器</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe61a;</i>
                    <router-link :to='{name: "Search", query:{search:"零食",rule:1,price:0,sales:0,index:1}}' class="h">零食</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"生鲜",rule:1,price:0,sales:0,index:1}}' class="h">生鲜</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"茶酒",rule:1,price:0,sales:0,index:1}}' class="h">茶酒</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe619;</i>
                    <router-link :to='{name: "Search", query:{search:"厨具",rule:1,price:0,sales:0,index:1}}' class="h">厨具</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"收纳",rule:1,price:0,sales:0,index:1}}' class="h">收纳</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"清洁",rule:1,price:0,sales:0,index:1}}' class="h">清洁</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe60a;</i>
                    <router-link :to='{name: "Search", query:{search:"家纺",rule:1,price:0,sales:0,index:1}}' class="h">家纺</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"家饰",rule:1,price:0,sales:0,index:1}}' class="h">家饰</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"鲜花",rule:1,price:0,sales:0,index:1}}' class="h">鲜花</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe65c;</i>
                    <router-link :to='{name: "Search", query:{search:"图书音像",rule:1,price:0,sales:0,index:1}}' class="h">图书音像</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"文具",rule:1,price:0,sales:0,index:1}}' class="h">文具</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe646;</i>
                    <router-link :to='{name: "Search", query:{search:"医药保健",rule:1,price:0,sales:0,index:1}}' class="h">医药保健</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"进口",rule:1,price:0,sales:0,index:1}}' class="h">进口</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe71d;</i>
                    <router-link :to='{name: "Search", query:{search:"汽车",rule:1,price:0,sales:0,index:1}}' class="h">汽车</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"二手车",rule:1,price:0,sales:0,index:1}}' class="h">二手车</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"用品",rule:1,price:0,sales:0,index:1}}' class="h">用品</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe660;</i>
                    <router-link :to='{name: "Search", query:{search:"房产",rule:1,price:0,sales:0,index:1}}' class="h">房产</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"装修家具",rule:1,price:0,sales:0,index:1}}' class="h">装修家具</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"建材",rule:1,price:0,sales:0,index:1}}' class="h">建材</router-link>
                </li>
                <li>
                    <i class="font iconfont h">&#xe62c;</i>
                    <router-link :to='{name: "Search", query:{search:"手表",rule:1,price:0,sales:0,index:1}}' class="h">手表</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"眼镜",rule:1,price:0,sales:0,index:1}}' class="h">眼镜</router-link>
                    <span class="h">/</span>
                    <router-link :to='{name: "Search", query:{search:"珠宝饰品",rule:1,price:0,sales:0,index:1}}' class="h">珠宝饰品</router-link>
                </li>
            </ul>
        </div>
        <div id="central_navigation">
            <div id="central_navigation_one">
                <div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
                  <div class="carousel-inner">
                    <div class="carousel-item active">
                      <img src="@/assets/RotationOne/six.jpeg" style="width: 520px;height: 280px;" class="d-block w-100 rotation" alt="...">
                    </div>
                    <div class="carousel-item">
                      <img src="@/assets/RotationOne/two.jpeg" style="width: 520px;height: 280px;" class="d-block w-100 rotation" alt="...">
                    </div>
                    <div class="carousel-item">
                      <img src="@/assets/RotationOne/three.jpeg" style="width: 520px;height: 280px;" class="d-block w-100 rotation" alt="...">
                    </div>
                    <div class="carousel-item">
                      <img src="@/assets/RotationOne/four.jpeg" style="width: 520px;height: 280px;" class="d-block w-100 rotation" alt="...">
                    </div>
                    <div class="carousel-item">
                      <img src="@/assets/RotationOne/five.png" style="width: 520px;height: 280px;" class="d-block w-100 rotation" alt="...">
                    </div>
                  </div>
                  <button class="carousel-control-prev btn_one font iconfont" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
                    &#xeb9b;
                  </button>
                  <button class="carousel-control-next btn_two font iconfont" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
                    &#xe62e;
                  </button>
                </div>
            </div>
            <div id="current_page">
                <span>YouGou</span>
                <i>优质购物上优购</i>
                <i><em ref="index">1 </em> / 5</i>
            </div>
            <div id="central_navigation_two">
                <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel" @[`slid.bs.carousel`]="getRotationPage">
                  <div class="carousel-inner">
                    <div class="carousel-item active"  data-index="1">
                      <!--{# 占位 #}-->
                      <div class="seize_a_seat">
                        <img src="@/assets/RotationTwo/one.jpg" alt=""/>
                        <img src="@/assets/RotationTwo/two.jpg" alt=""/>
                      </div>
                    </div>
                    <div class="carousel-item"  data-index="2">
                      <!--{# 占位 #}-->
                      <div class="seize_a_seat">
                          <img src="@/assets/RotationTwo/three.jpg" alt="" style="height: 155px;"/>
                          <img src="@/assets/RotationTwo/four.jpeg" alt="" style="height: 155px;"/>
                      </div>
                    </div>
                    <div class="carousel-item"  data-index="3">
                      <!--{# 占位 #}-->
                      <div class="seize_a_seat">
                          <img src="@/assets/RotationTwo/five.jpeg" alt="" />
                          <img src="@/assets/RotationTwo/six.jpg" alt="" />
                      </div>
                    </div>
                    <div class="carousel-item"  data-index="4">
                      <!--{# 占位 #}-->
                      <div class="seize_a_seat">
                          <img src="@/assets/RotationTwo/seven.jpg" alt="" />
                          <img src="@/assets/RotationTwo/eight.jpg" alt="" />
                      </div>
                    </div>
                    <div class="carousel-item"  data-index="5">
                      <!--{# 占位 #}-->
                      <div class="seize_a_seat">
                          <img src="@/assets/RotationTwo/nine.jpg" alt="" />
                          <img src="@/assets/RotationTwo/ten.jpg" alt="" />
                      </div>
                    </div>
                  </div>
                  <button class="carousel-control-prev btn_one font iconfont" type="button" data-bs-target="#carouselExampleCaptions" @[`slid.bs.carousel`]="getRotationPage" data-bs-slide="prev">
                    &#xeb9b;
                  </button>
                  <button class="carousel-control-next btn_two font iconfont" type="button" data-bs-target="#carouselExampleCaptions" @[`slid.bs.carousel`]="getRotationPage" data-bs-slide="next">
                    &#xe62e;
                  </button>
                </div>
            </div>
        </div>
        <div id="user_information">
            <!--{# 头部 #}-->
            <div class="user_information_head">
                <router-link :to="{name: 'user'}">
                    <img :src="user_image?user_image:'https://w.wallhaven.cc/full/e7/wallhaven-e7lomr.jpg'" alt="" />
                </router-link>
                <router-link :to="{name: 'user'}">
                    <span>Hi!</span>
                    <span style="font-weight: bold;">{{username?username:'你好'}}</span>
                </router-link>
                <ul v-if="shop_info">
                  <li v-for="(item, index) in shop_info" :key="index">
                      <router-link :to="{name: personal[index]}">
                          <span>{{item.num}}</span><i>{{item.status}}</i>
                      </router-link>
                  </li>
                </ul>
                <div v-else class="member-ft">
                  <router-link :to="{name: 'Login'}"><div>登录</div></router-link>
                  <router-link :to="{name: 'Register'}"><div>注册</div></router-link>
                  <div>开店</div>
                </div>
            </div>
            <!--{# 轮播图 #}-->
            <div class="merry_go_round">
                <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
                  <div class="carousel-inner">
                    <div class="carousel-item active">
                      <img src="@/assets/RotationThree/one.png" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                      <img src="@/assets/RotationThree/two.jpeg" class="d-block w-100" alt="...">
                    </div>
                  </div>
                </div>
            </div>
            <!--{# 新闻导航 #}-->
            <div id="notice">
                <div class="times">
                  <span>{{year}}年{{month}}月{{date}}号{{week[day-1]}}</span>
                  <span>{{hours}}:{{minute}}</span>
                </div>
                <video autoplay loop muted>
                  <source src="@/assets/backImage/one.mp4" type="video/mp4" />
                </video>
            </div>
            <!--{# 底部导航 #}-->
            <div id="bottom_nav">
                <a href="#">
                    <i class="bot iconfont">&#xe733;</i>
                    <span>收藏的宝贝</span>
                </a>
                <a href="#">
                    <i class="bot iconfont">&#xe8bb;</i>
                    <span>买过的店铺</span>
                </a>
                <a href="#">
                    <i class="bot iconfont">&#xe895;</i>
                    <span>收藏的店铺</span>
                </a>
                <a href="#">
                    <i class="bot iconfont">&#xe662;</i>
                    <span>我的足迹</span>
                </a>
            </div>
        </div>
    </article>
</template>

<script>
import jwtDecode from 'jwt-decode'

export default {
  name: 'navigation',
  data () {
    return {
      year: '',
      month: '',
      date: '',
      day: '',
      username: '',
      user_image: '',
      minute: '',
      hours: '',
      shop_info: '',
      week: ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天'],
      personal: ['shopcart', 'payoff', 'delivery', 'receiving', 'evaluate']
    }
  },
  methods: {
    getRotationPage (e) {
      const index = e.target.querySelector('.active').getAttribute('data-index')
      try {
        this.$refs.index.innerHTML = index
      } catch (e) {
      }
    },
    getTime () {
      /* 指定时间 */
      let nowdate = new Date()
      this.year = nowdate.getFullYear() // 年
      this.month = nowdate.getMonth() + 1 // 月
      this.date = nowdate.getDate() // 号
      this.day = nowdate.getDay() // 星期
      this.minute = nowdate.getMinutes() < 10 ? '0' + nowdate.getMinutes() : nowdate.getMinutes()
      this.hours = nowdate.getHours() < 10 ? '0' + nowdate.getHours() : nowdate.getHours()
    },
    // 获取用户购物信息
    getShoppingInfo () {
      this.$https.post('store/shopping/').then(res => {
        if (res.data.code === 200) {
          this.shop_info = res.data.data.shop_info
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted () {
    setTimeout(() => {
      this.getTime()
    })
    setInterval(() => {
      this.getTime()
    }, 6000)
  },
  created () {
    this.getShoppingInfo()
    try {
      const decode = jwtDecode(this.$store.state.token)
      this.username = decode.username
      this.user_image = decode.img
    } catch (e) {

    }
  }
}
</script>

<style scoped lang="less">

#side_nav {
  width: 1155px;
  height: 575px;
  display: flex;
  justify-content: space-between;
  background-color: #f2f2f2;
  padding: 25px 0;
  border-radius: 15px;
  margin: 0 auto 45px;
  #bulletin_board {
    color: #666666;
    font-size: 14px;
    height: 510px;
    width: 194px;
    ul {
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      height: 510px;
      width: 194px;
      margin: 6px 0 3px 18px;
      padding: 0;
      .font {
        font-size:16px;
        margin-right: 10px;
      }
      li {
        height: 20px;
        line-height: 20px;
        text-align: left;
        &:hover .h{
          color: #FF3701;
        }
        a {
          color: #666666;
          font-size: 14px;
          text-decoration: none;
          &:hover {
            text-decoration: underline;
          }
        }
        span {
          padding: 0 3px;
        }
      }
    }
  }
}

#central_navigation {
  width: 520px;
  height: 512px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;

  #central_navigation_one {
    min-width: 520px;
    height: 280px;
    border-radius: 15px;
    overflow: hidden;
    margin-top: 6px;
    position: relative;
    &:hover button{
      display: block;
    }
  }
  #central_navigation_two {
    min-width: 520px;
    height: 201px;
    border-radius: 15px;
    position: relative;
    &:hover button{
      display: block;
    }
    img {
      width: 251px;
      height: 190px;
      border-radius: 15px;
    }
    .carousel-caption {
      right: 0;
      left: 0;
      padding: 0;
      width: 520px;
      height: 201px;
      bottom: 0;
    }
    .seize_a_seat {
      min-width: 520px;
      height: 201px;
      display: flex;
      justify-content: space-around;
      align-items: center;
      background-color: #fff;
      border-radius: 15px;
    }
  }
}

#central_navigation_one button,  #central_navigation_two button{
    height: 30px;
    width: 20px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    background-color: rgba(0,0,0,.3);
    margin: 0;
    display: none;
}

.btn_one {
    border-bottom-right-radius: 15px;
    border-top-right-radius: 15px;
    text-align: left;
}
.btn_two {
    border-bottom-left-radius: 15px;
    border-top-left-radius: 15px;
    text-align: right;
}
#current_page {
  text-align: left;
  height:24px;
  width: 100%;
  margin-top: 10px;
  span {
    color: #FF0136;
    font-weight: bold;
    margin-right: 5px;
  }
  i:last-child {
    float: right;
    color: #3c3c3c;
  }
  i {
    font-style: normal;
    font-size: 12px;
    color: #999;
    line-height: 24px;
  }
  em {
    font-style: normal;
    color: #FF1648;
  }
}

#user_information {
    background-color: #E5E5E5;
    width: 384px;
    height: 508px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    border-radius: 15px;
}
.user_information_head {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 15px;
  .member-ft {
    display: flex;
    justify-content: space-between;
    width: 356px;
    margin-top: 10px;
    div {
      color: #fff;
      background-color: #E1251B;
      width: 105px;
      height: 32px;
      line-height: 32px;
      text-align: center;
      border-radius: 7px;
      cursor: pointer;
      font-size: 14px;
    }
  }
  img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 1px solid #FABF9E;
  }
  a {
    text-decoration: none;
    span {
      font-size: 12px;
      color: #3c3c3c;
    }
  }
  ul {
    display: flex;
    align-items: center;
    justify-content: space-around;
    padding-left: 14px;
    width: 90%;
    margin-top: 10px;
  }
  li {
    a {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      &:hover i{
        color: #f40;
      }
    }
    i {
      font-size: 12px;
      color: #3c3c3c;
      font-style: normal;
    }
    span {
      font-size: 14px;
      color: #f40;
      font-weight: bold;
    }
  }

}
.merry_go_round {
  width: 356px;
  height: 141px;
  border-radius: 5px;
  overflow: hidden;
  margin: 0 auto;
}
#notice {
  height: 125px;
  padding: 15px;
  position: relative;
  overflow: hidden;
  &:hover video{
    filter: blur(1px); //背景模糊设置
  }
  .times {
    z-index: 999;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    color: #fff;
    width: 100%;
    display: flex;
    flex-direction: column;
    span {
      font-size: 16px;
      color: #28375F;
      text-shadow:1px 1px 1px #fff;
    }
  }
  video {
    width: 355px;
    position: absolute;
    z-index: 1;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    border-radius: 15px;
    // -webkit-filter: grayscale(100%);
    // filter:grayscale(100%); //背景灰度设置*/
  }
  //video {
  //  position: fixed;
  //  right: 0px;
  //  bottom: 0px;
  //  min-width: 100%;
  //  min-height: 100%;
  //  height: auto;
  //  width: auto;
  //  z-index: -1;
  //  source{
  //    min-width: 100%;
  //    min-height: 100%;
  //    height: auto;
  //    width: auto;
  //  }
  //}
}

#bottom_nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-left: 12px;
  margin-bottom: 15px;
  a {
    text-decoration: none;
    font-size: 12px;
    color: #333;
    display: flex;
    width: 60px;
    height: 53px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    i {
      font-size: 21px;
    }
    &:hover i{
      color: #FF6E07;
    }
  }
}
</style>
