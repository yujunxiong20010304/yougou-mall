<template>
  <div id="home">
    <all-header></all-header>
    <all-search></all-search>
    <navigation></navigation>
    <seckill></seckill>
    <very-goods></very-goods>
    <channel-square></channel-square>
    <recommend :msg="goods_info"></recommend>
    <all-tail></all-tail>
    <el-backtop :bottom="100" :right="15">
      <img src="@/assets/backImage/rocket.png" alt="" style="height: 100%;width: 100%;"/>
    </el-backtop>
  </div>
</template>

<script>
import navigation from '@/components/shop/navigation'
import seckill from '@/components/shop/seckill'
import ChannelSquare from '@/components/shop/ChannelSquare'
import recommend from '@/components/shop/recommend'
import VeryGoods from '@/components/shop/VeryGoods'
import emitter from '@/utils/event'
export default {
  name: 'Home',
  components: {
    'very-goods': VeryGoods,
    navigation,
    seckill,
    'channel-square': ChannelSquare,
    recommend
  },
  data () {
    return {
      goods_info: '',
      aim: 0,
      recommend: ['数码', '电器', '家居', '生鲜', '美妆', '手机', '电脑']
    }
  },
  methods: {
    async getGoodsInfo (theme) {
      const { data: res } = await this.$http.post('store/goods/', { theme: theme, number: 48, interval: 0 })
      if (res.code === 200) {
        this.goods_info = res.data
      }
    }
  },
  created () {
    this.getGoodsInfo('数码')
    emitter.on('recommend', (e) => {
      this.aim = e.aim
    })
  },
  watch: {
    aim: {
      handler (newVal, oldVal) {
        let theme = this.recommend[newVal]
        this.getGoodsInfo(theme)
      },
      immediate: true
    }
  }
}
</script>

<style scoped lang="less">
#home {
  background-color: #fff;
}
:deep(.el-backtop) {
  box-shadow: none;
  &:hover {
    background-color: rgba(255, 255, 255, .1);
  }
}
</style>
