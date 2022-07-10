<template>
  <div id="yougou">
    <!-- 可以展示的用户数据 用户名， 头像， 邮箱， 余额 -->
    <div class="user">
      <div class="info">
        <div class="head-port" :style="{backgroundImage: 'url('+user_info?.user_image+')'}">
          <span @click="upload_avatar">编辑头像</span>
        </div>
        <div class="user-info">
          <span >优购会员 <span style="margin-left: 5px;">({{user_info.username}})</span></span>
          <span>资料完整度:<span class="speed"><i>50%</i></span></span>
          <span>账户安全级别:<span style="font-size: 14px;font-weight: 400;color: red;padding-left: 5px;">低</span></span>
        </div>
      </div>
      <div class="coupons">
        <span>优惠卷：<i>0</i></span>
        <span>优购卡：<i>¥ 0.00</i></span>
        <span>优购币：<i>0</i></span>
        <span>零钱余额：<i>¥ {{user_info?.balance}}.00</i></span>
      </div>
    </div>
    <div class="ripple"></div>
    <div class="seize">
      <div class="my-order common">
        <div class="title">我的订单</div>
        <ul>
          <li @mouseover="moveIn(0)" @mouseout="moveOut">
            <div :style="{backgroundPosition:(aim===0?'0 0':'-74px 0')}"></div><!-- 0 0 -->
            <span ref="">退换/售后</span>
          </li>
          <li @mouseover="moveIn(1)" @mouseout="moveOut">
            <div :style="{backgroundPosition:(aim===1?'-148px 0':'-148px -74px')}"></div><!-- -148 0 -->
            <span>待付款</span>
          </li>
          <li @mouseover="moveIn(2)" @mouseout="moveOut">
            <div :style="{backgroundPosition:(aim===2?'0 -148px':'-74px -148px')}"></div><!-- 0 -148 -->
            <span>待收货</span>
          </li>
          <li @mouseover="moveIn(3)" @mouseout="moveOut">
            <div :style="{backgroundPosition:(aim===3?'-148px -148px':'-222px 0')}"></div><!-- -148 -148 -->
            <span>待发货</span>
          </li>
          <li @mouseover="moveIn(4)" @mouseout="moveOut">
            <div :style="{backgroundPosition:(aim===4?'0 -74px':'-74px -74px')}"></div><!-- 0 -74 -->
            <span>全部订单</span>
          </li>
        </ul>
      </div>
      <div class="my-follow common">
        <div class="calendar">我的日历</div>
        <div class="date">
          <span class="number">{{date}}</span>
          <span>{{week[day]}}</span>
          <span>{{year}}.{{month>10?month:'0'+month}}</span>
        </div>
      </div>
    </div>
    <transition name="el-zoom-in-top">
      <headportrait v-show="show" class="transition-box"></headportrait>
    </transition>
  </div>
</template>

<script>
import headportrait from '@/components/user/HeadPortrait'
import emitter from '@/utils/event'
export default {
  name: 'YouGou',
  components: {
    headportrait: headportrait
  },
  data () {
    return {
      aim: '',
      user_info: '',
      week: ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天'],
      year: '',
      month: '',
      date: '',
      day: '',
      show: false
    }
  },
  methods: {
    // 上传头像
    upload_avatar () {
      this.show = true
      emitter.on('show', (e) => {
        this.show = e.aim
      })
      emitter.on('image', (e) => {
        this.user_info.user_image = e.aim.url
      })
    },
    // 发送axios获取用户数据
    getUserInfo () {
      this.$https.post('store/user/').then(res => {
        if (res.data.code === 200) {
          this.user_info = res.data.data
        }
      }).catch(err => {
        console.log(err)
      })
    },
    moveIn (index) {
      this.aim = index
    },
    moveOut () {
      this.aim = ''
    }
  },
  created () {
    this.getUserInfo()
    let nowdate = new Date()
    this.year = nowdate.getFullYear() // 年
    this.month = nowdate.getMonth() + 1 // 月
    this.date = nowdate.getDate() // 号
    this.day = nowdate.getDay() // 星期
  }
}
</script>

<style scoped lang="less">
#yougou {
  width: 100%;
  text-align: left;
  height: 100%;
  position: relative;
  .user {
    width: 100%;
    height: 179px;
    border: 1px solid #ccc;
    display: flex;
    padding: 7px;
    flex-direction: column;
    background-image: linear-gradient(to right,rgba(249,249,249,1),rgba(255,255,255,.5)),url('../../assets/verygoods/test.jpeg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    .info {
      display: flex;
      .head-port {
        width: 100px;
        height: 100px;
        overflow: hidden;
        position: relative;
        border-radius: 50%;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        border: 4px solid white;
        box-sizing: content-box;
        box-shadow:0 15px 35px
        rgba(255,255,255,0.2),0 2px 5px
        rgba(255,255,255,0.2);
        span {
          width: 100px;
          text-align: center;
          font-size: 12px;
          position: absolute;
          color: white;
          background-color: rgba(0,0,0,.7);
          left: 50%;
          bottom: -20px;
          transform: translate(-50%, 0);
          transition: bottom .2s ease;
          cursor: pointer;
        }
        &:hover span{
          bottom: 0;
        }
      }
      .user-info {
        width: 220px;
        height: 95px;
        font-size: 14px;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        padding-left: 10px;
        .speed {
          display: inline-block;
          width: 90px;
          height: 12px;
          background-color: #ddd;
          position: relative;
          margin-left: 5px;
          i {
            position: absolute;
            display: inline-block;
            width: 45px;
            height: 100%;
            background-color: #00b3ee;
            font-size: 12px;
            color: #fff;
            font-style: normal;
            font-weight: 300;
            text-align: center;
            line-height: 12px;
          }
        }
        span {
          color: #666;
          display: flex;
          align-items: center;
          &:first-child {
            font: 700 16px 'Microsoft Yahei',Arial;
            color: #333;
            span {
              font-size: 14px;
              font-weight: 400;
            }
          }
        }
      }
    }
  }
  .coupons {
    width: 698px;
    background-color: #EEF4F9;
    height: 42px;
    padding: 12px;
    display: flex;
    align-items: center;
    justify-content: space-around;
    span {
      font-size: 12px;
      color: #666;
      i {
        font-style: normal;
        font-weight: bold;
        color: #000;
      }
    }
  }
  .ripple {
    width: 100%;
    // background-color: springgreen;
    height: 5px;
    background-image: url('../../assets/verygoods/outline.png');
  }

  .seize {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    .my-order {
      width: 75%;
      min-width: 700px;
      ul {
        display: flex;
        align-items: center;
        width: 100%;
        height: 206px;
        justify-content: space-around;
        padding: 0;
        margin: 0;
        li {
          display: flex;
          justify-content: center;
          flex-direction: column;
          height: 111px;
          cursor: pointer;
          &:hover span{
            color: #F11988;
          }
          div {
            background-image: url('../../assets/verygoods/state.png');
            width: 70px;
            height: 70px;
          }
          span {
            text-align: center;
            font-size: 14px;
            color: #333;
            padding-top: 20px;
          }
        }
      }
    }
    .my-follow {
      width: 286px;
      margin-left: 15px;
      .calendar {
        background-color: #6EC885;
        width: 100%;
        height: 44px;
        color: #fff;
        text-align: center;
        line-height: 44px;
      }
      .date {
        height: 204px;
        justify-content: center;
        align-items: center;
        display: flex;
        flex-direction: column;
        font-size: 15px;
        color: #55B46C;
        background-color: #F8FFFA;
        .number {
          font-size: 60px;
          font-weight: bold;
        }
      }
    }
    .common {
      height: 250px;
      margin-top: 25px;
      border: 1px solid #ccc;
      .title {
        width: 100%;
        height: 44px;
        background-color: #f9f9f9;
        display: flex;
        align-items: center;
        font-size: 14px;
        font-weight: 700;
        padding-left: 32px;
        position: relative;
        border-bottom: 1px #ececec solid;
        &:before {
          content: '';
          position: absolute;
          display: block;
          width: 2px;
          height: 14px;
          background-color: #409EFF;
          left: 20px;
        }
      }
    }
  }
}
</style>
