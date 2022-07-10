<template>
  <div :style="{ height: height + 'px' }">
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: 'App',
  data () {
    return {
      height: ''
    }
  },
  mounted () {
    // 设置窗口大小
    this.height = document.documentElement.clientHeight
    window.onresize = () => {
      return (() => {
        this.height = document.documentElement.clientHeight
      })()
    }
  },
  methods: {
    async getEncryption () {
      const { data: res } = await this.$http.post('oauth/public_key/')
      if (res.code === 200) {
        this.$store.commit('GetPublicKey', res.data)
      }
    }
  },
  // 初始化获取加密公钥
  created () {
    this.getEncryption()
  }
}
</script>
<style lang="less">
* {
  margin: 0;
  padding: 0;
  list-style-type: none;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
// 阿里图标字体
@font-face {
  font-family: 'iconfont';  /* Project id 3203454 */
  src: url('//at.alicdn.com/t/font_3203454_rawi2az7n4.woff2?t=1654571323862') format('woff2'),
       url('//at.alicdn.com/t/font_3203454_rawi2az7n4.woff?t=1654571323862') format('woff'),
       url('//at.alicdn.com/t/font_3203454_rawi2az7n4.ttf?t=1654571323862') format('truetype');
}
</style>
