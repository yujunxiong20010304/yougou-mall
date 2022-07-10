<template>
<!-- 秒杀 -->
  <div id="count-down">
    <div id="seckill">
      <h5>限时秒杀</h5>
      <div class="time">
        <span><strong>12:00</strong> 点场 距结束</span>
        <ul>
          <li>{{h}}</li>
          <li>:</li>
          <li>{{m}}</li>
          <li>:</li>
          <li>{{s}}</li>
        </ul>
      </div>
    </div>
    <!-- 轮播图 -->
    <div id="seckill-shop">
      <div id="central_navigation_three">
        <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <!--{# 占位 #}-->
              <div class="seize_a_seat">
                <div class="shop" v-for="item in shop_list.slice(0, 4)" @click="enterDetail(item.id)">
                  <img :src="item.goods_image" alt="" />
                  <h6>{{item.title}}</h6>
                  <span>¥ 36.26</span>
                </div>
              </div>
            </div>
            <div class="carousel-item">
              <!--{# 占位 #}-->
              <div class="seize_a_seat">
                <div class="shop" v-for="item in shop_list.slice(4, 8)" @click="enterDetail(item.id)">
                  <img :src="item.goods_image" alt="" />
                  <h6>{{item.title}}</h6>
                  <span>¥ 36.26</span>
                </div>
              </div>
            </div>
            <div class="carousel-item">
              <!--{# 占位 #}-->
              <div class="seize_a_seat">
                <div class="shop" v-for="item in shop_list.slice(8, 12)" @click="enterDetail(item.id)">
                  <img :src="item.goods_image" alt="" />
                  <h6>{{item.title}}</h6>
                  <span>¥ 36.26</span>
                </div>
              </div>
            </div>
            <div class="carousel-item">
              <!--{# 占位 #}-->
              <div class="seize_a_seat">
                <div class="shop" v-for="item in shop_list.slice(12, 16)" @click="enterDetail(item.id)">
                  <img :src="item.goods_image" alt="" />
                  <h6>{{item.title}}</h6>
                  <span>¥ 36.26</span>
                </div>
              </div>
            </div>
            <div class="carousel-item">
              <!--{# 占位 #}-->
              <div class="seize_a_seat">
                <div class="shop" v-for="item in shop_list.slice(16, 20)" @click="enterDetail(item.id)">
                  <img :src="item.goods_image" alt="" />
                  <h6>{{item.title}}</h6>
                  <span>¥ 36.26</span>
                </div>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev btn_one font iconfont" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
            &#xeb9b;
          </button>
          <button class="carousel-control-next btn_two font iconfont" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
            &#xe62e;
          </button>
        </div>
      </div>
    </div>
    <!--  二号轮播  -->
    <div id="slider">
      <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="slider_item">
              <img src="@/assets/backImage/phone1.jpeg" alt="">
              <h6>真维斯秒杀专场</h6>
              <h5>全场低至59元</h5>
              <div>品牌秒杀<span class="iconfont">&#xe642;</span></div>
            </div>
          </div>
          <div class="carousel-item">
            <div class="slider_item">
              <img src="@/assets/backImage/phone2.jpeg" alt="">
              <h6>真维斯秒杀专场</h6>
              <h5>全场低至59元</h5>
              <div>品牌秒杀<span class="iconfont">&#xe642;</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'seckill',
  data () {
    return {
      shop_list: '',
      timer: '',
      h: 11,
      m: 59,
      s: 59
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
    CountDown () {
      /* 指定时间 */
      let end = 60 * 60 * 12 * 1000 + +new Date()
      this.timer = setInterval(() => {
        let date = +new Date()
        let time = (end - date) / 1000
        let h = parseInt(time / 60 / 60 % 24)
        let m = parseInt(time / 60 % 60)
        let s = parseInt(time % 60)
        h = h >= 10 ? h : '0' + h
        m = m >= 10 ? m : '0' + m
        s = s >= 10 ? s : '0' + s
        this.h = h
        this.m = m
        this.s = s
      }, 1000)
    },
    async LimitTimeSpike () {
      const { data: res } = await this.$http.post('store/goods/', { theme: '衣服', number: 20, interval: 0 })
      if (res.code === 200) {
        this.shop_list = res.data
      }
    }
  },
  created () {
    this.LimitTimeSpike()
  },
  mounted () {
    this.CountDown()
  },
  beforeUnmount () {
    clearInterval(this.timer)
    this.timer = null
  }
}
</script>

<style scoped lang="less">
#count-down {
  display: flex;
  justify-content: center;
  width: 1155px;
  margin: 0 auto;
  #seckill {
    width: 190px;
    height: 260px;
    background-image: url('../../assets/backImage/seckill.png');
    background-size: 190px 260px;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    color: white;
    h5 {
      font-size: 30px;
      margin-top: 30px;
    }
    .time {
      margin-bottom: 30px;
      span {
        font-size: 14px;
        strong {
          font-size: 18px;
          font-weight: 400;
        }
      }
      ul {
        margin: 5px auto 0;
        width: 100%;
        display: flex;
        justify-content: center;
        padding: 0;
        li:nth-child(odd) {
          width: 30px;
          height: 30px;
          background-color: black;
          font-size: 20px;
          text-align: center;
          line-height: 30px;
        }
        li:nth-child(even) {
          width: 20px;
          font-size: 25px;
          line-height: 30px;
        }
      }
    }
  }

  #seckill-shop {
    width: 794px;
    height: 260px;
    // 轮播
    #central_navigation_three {
      min-width: 520px;
      height: 201px;
      position: relative;
      &:hover button{
        display: block;
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
        height: 260px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #fff;
        .shop {
          width: 203px;
          height: 260px;
          padding: 30px 31.6px;
          cursor: pointer;
          &:hover h6{
            color: #e1251b;
          }
          &:hover img {
            opacity: .8;
          }
          img {
            width: 140px;
            height: 140px;
          }
          h6 {
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            font-size: 12px;
            color: #333;
            font-weight: 400;
            padding-top: 13px;
          }
          span {
            font-size: 12px;
            color: #e1251b;
            font-weight: 700;
          }
        }
      }
      button {
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
    }
  }

  #slider {
    width: 170px;
    height: 260px;
    .slider_item {
      height: 260px;
      padding: 10px;
      font-size: 14px;
      background: linear-gradient(180deg,rgba(255,255,255,1),rgba(220,224,236,1));
      img {
        width: 120px;
        height: 120px;
      }
      h6 {
        color: #666;
        font-weight: 400;
        font-size: 14px;
        padding-top: 15px;
      }
      h5 {
        font-size: 14px;
        font-weight: 500;
        color: #333;
        padding-top: 10px;
      }
      div {
        border: 1px solid #e1251b;
        width: 82px;
        height: 24px;
        border-radius: 12px;
        margin: 0 auto;
        font-size: 12px;
        color: #e1251b;
        line-height: 24px;
        font-weight: 500;
        cursor: pointer;
        margin-top: 10px;
      }
    }
  }
}
</style>
