<template>
<!-- 发现好货 -->
  <div id="very-goods" @mouseover="stopRotation" @mouseout="veryGoodsRotation">
    <div id="left-side">
      <div>
        <span>探索新生活<i></i></span>
      </div>
    </div>
    <div id="right-side" @mouseover="showPulley" @mouseout="hidePulley">
      <div class="content">
        <ul ref="rolling">
          <li v-for="(item,index) in shop_list" @click="enterDetail(item.id)">
            <span v-if="index%2==0">{{item.title}}</span>
            <img :src="item.goods_image" alt="" />
            <span v-if="index%2!=0">{{item.title}}</span>
          </li>
        </ul>
      </div>
      <div id="pulley">
        <div ref="pulley">
          <span ref="wheel" @mousedown="pulleyWheel"></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'verygoods',
  data () {
    return {
      timer: null,
      position: 0,
      shop_list: ''
    }
  },
  methods: {
    enterDetail (id) {
      const newpage = this.$router.resolve({
        path: '/detail', // 跳转的页面路由
        query: { // 要传的参数
          id: id
        }
      })
      window.open(newpage.href, '_blank')
    },
    async FindGoods () {
      const { data: res } = await this.$http.post('store/goods/', { theme: '零食', number: 75, interval: 5 })
      if (res.code === 200) {
        this.shop_list = res.data
      }
    },
    // 定时器进行滚动
    veryGoodsRotation () {
      this.timer = setInterval(() => {
        try {
          this.position = this.$refs.rolling.offsetLeft
          // this.position = this.$refs.rolling.offsetLeft
          this.$refs.rolling.style.left = --this.position + 'px'
          if (this.position < -1899) {
            this.$refs.rolling.style.left = 0 + 'px'
          }
        } catch (e) {
          clearInterval(this.timer)
        }
      }, 20)
    },
    // 停止滚动
    stopRotation () {
      clearInterval(this.timer)
    },
    // 底部滑轮拖动
    pulleyWheel (e) {
      let disx = e.clientX - this.$refs.wheel.offsetLeft
      let ts = this
      document.onmousemove = function (event) {
        let state = ts.$refs.pulley.style.display
        let judge = parseInt(ts.$refs.wheel.style.left.split('p')[0])
        if (judge <= 835 && judge >= 0 && state === 'block') {
          ts.$refs.wheel.style.left = event.clientX - disx + 'px'
          ts.$refs.rolling.style.left = -(event.clientX - disx) * 2.27 + 'px'
          ts.position = -(event.clientX - disx) * 2.27
        }
      }
      document.onmouseup = function () {
        // 这俩都要置为null
        document.onmousemove = null
        document.onmouseup = null
        return false
      }
    },
    // 滑轮显示
    showPulley () {
      this.$refs.pulley.style.display = 'block'
      this.$refs.wheel.style.left = Math.abs(this.position) / 2.27 + 'px'
    },
    // 滑轮隐藏
    hidePulley () {
      this.$refs.pulley.style.display = 'none'
    }
  },
  mounted () {
    this.veryGoodsRotation()
  },
  deactivated () {
    // 页面关闭（路由跳转）时清除定时器
    clearInterval(this.timer)
    this.timer = null
  },
  created () {
    this.FindGoods()
  }
}
</script>

<style scoped lang="less">
#very-goods {
  margin: 35px auto 0;
  width: 1155px;
  display: flex;
  justify-content: space-between;
  #left-side {
    width: 190px;
    height: 260px;
    background-image: url('../../assets/backImage/2.jpg');
    padding-top: 15px;
    background-size: cover;
    background-position: center;
    cursor: pointer;
    div {
      width: 160px;
      height: 89px;
      margin: 0 auto;
      background-color: rgba(0,0,0, .5);
      border-bottom-right-radius: 21px;
      background-image: url('../../assets/backImage/very-goods.png');
      background-position: center;
      background-size: cover;
      position: relative;
      span {
        color: rgba(255,255,255,.8);
        font-size: 16px;
        position: absolute;
        bottom: 11px;
        left: 20px;
        display: flex;
        align-items: center;
        i {
          margin-left: 7px;
          background-image: url('../../assets/backImage/arrow.png');
          display: block;
          width: 16px;
          height: 16px;
          background-position: 0 -16px;
          background-size: 32px;
        }
      }
    }
    &:hover i{
      background-position: 0 0;
    }
  }
}
#right-side {
  width: 955px;
  height: 260px;
  background: #fff;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  overflow: hidden;
  .content {
    width: 910px;
    margin: 0 auto;
    position: relative;
    height: 231px;
    ul {
      margin: 0;
      padding: 0;
      display: flex;
      position: absolute;
      li {
        width: 150px;
        height: 181px;
        font-size:0;
        &:hover span{
          color: #E46166;
        }
        &:hover img {
          opacity: .8;
        }
        img {
          width: 150px;
          height: 150px;
        }
        span {
          width: 150px;
          height: 21px;
          display: inline-block;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
          color: #333;
          text-align: center;
          font-size: 14px;
          font-weight: 400;
        }
      }
      li:nth-child(odd) {
        margin: 50px 40px 0 0;
        span {
          margin-bottom: 10px;
        }
      }
      li:nth-child(even) {
        margin: 20px 40px 0 0;
        span {
          margin-top: 10px;
        }
      }
    }
  }
  #pulley {
    width: 955px;
    height: 29px;
    padding: 13px 0;
    div {
      width: 915px;
      height: 3px;
      background-color: #d8d8d8;
      border-radius: 3px;
      margin: 0 auto;
      position: relative;
      display: none;
      span {
        width: 79px;
        height: 9px;
        background-color: #d8d8d8;
        border-radius: 6px;
        position: absolute;
        top: 50%;
        left: 0;
        transform: translate(0, -50%);
      }
    }
  }
}
</style>
