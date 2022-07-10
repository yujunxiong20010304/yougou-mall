<template>
  <div id="track">
    <h6>看了又看</h6>
    <div id="track-container" ref="container">
      <ul class="track_all" ref="ul">
        <li class="track-alone" v-for="item in shops" :key="item.id" @click="enterDetail(item.id)">
          <img :src="item.goods_image" alt=""/>
          <div>{{ item.title }}</div>
          <p>￥ {{item.min_price}}.00</p>
        </li>
      </ul>
    </div>
    <div id="up-down">
      <i class="iconfont" @click="lower">&#xe62b;</i>
      <i class="iconfont" @click="upper">&#xeb9c;</i>
    </div>
  </div>
</template>

<script>
export default {
  name: 'shopRight',
  data () {
    return {
      judge: true,
      shops: ''
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
    async GetLookShop () {
      const { data: res } = await this.$http.post('store/goods/', { theme: '零食', number: 150, interval: 10 })
      if (res.code === 200) {
        this.shops = res.data
      }
    },
    lower () {
      if (this.judge) {
        this.judge = false
        let top = this.$refs.ul.offsetTop
        if (top !== -552 * 4) {
          this.$refs.ul.style.top = -552 + top + 'px'
        } else {
          this.$refs.ul.style.top = 0 + 'px'
        }
        setTimeout(() => {
          this.judge = true
        }, 700)
      }
    },
    upper () {
      if (this.judge) {
        this.judge = false
        let top = this.$refs.ul.offsetTop
        if (top !== 0) {
          this.$refs.ul.style.top = 552 + top + 'px'
        } else {
          this.$refs.ul.style.top = -552 * 4 + 'px'
        }
      }
      setTimeout(() => {
        this.judge = true
      }, 700)
    }
  },
  created () {
    this.GetLookShop()
  }
}
</script>

<style scoped lang="less">
#track {
  width: 210px;
  height: 644.5px;
}
#track h6 {
  color: #666;
  font-size: 14px;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}
h6::before {
  content: "";
  display: inline-block;
  width: 45px;
  border: 1px solid #f2f2f2;
  margin-right: 10px;
}
h6::after {
  content: "";
  display: inline-block;
  width: 45px;
  border: 1px solid #f2f2f2;
  margin-left: 10px;
}
#track-container {
  width: 208px;
  height: 549px;
  overflow: hidden;
  position: relative;
  margin-top: 15px;
}
.track_all {
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 552px;
  position: absolute;
  transform: translate(-50%, 0);
  left: 50%;
  top: 0;
  transition: all .7s;
}
.track-alone {
  position: relative;
}
.track-alone img{
  width:150px;
  height: 150px;
  cursor: pointer;
}
.track-alone div {
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  position: absolute;
  top: 126px;
  width: 138px;
  height: 12px;
  background: rgba(255,255,255,.9);
  font: 12px/150% tahoma,arial,Microsoft YaHei,Hiragino Sans GB,"\u5b8b\u4f53",sans-serif;
  color: #666;
  padding: 6px;
  box-sizing: content-box;
  line-height: 12px;
}
.track-alone p {
  color: #c81623;
  text-align: center;
  font: 12px/150% tahoma,arial,Microsoft YaHei,Hiragino Sans GB,"\u5b8b\u4f53",sans-serif;
  width: 150px;
  height: 18px;
  line-height: 18px;
}
#up-down {
  width: 210px;
  height: 29.5px;
  padding-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}
#up-down i {
  font-size: 26px;
  font-weight: bold;
  color: #ddd;
  margin: 0 10px;
  cursor: pointer;
}
</style>
