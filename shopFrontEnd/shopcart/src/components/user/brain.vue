<template>
  <div id="brain">
    <span
      class="iconfont stretch"
      @click="stretch(false)"
      :style="[judge?'display:inline-block':'display:none']">
      &#xe6a0;
    </span>
    <span
      class="iconfont stretch"
      @click="stretch(true)"
      :style="[judge?'display:none':'display:inline-block']">
      &#xe6a1;
    </span>
    <!-- 路径 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item v-for="(item, index) in navigation[address]" :key="index">{{item}}</el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script>
import emitter from '@/utils/event'

export default {
  name: 'brain',
  data () {
    return {
      judge: true,
      navigation: {
        yougou: ['我的优购'],
        shopcart: ['我的订单', '购物车'],
        payoff: ['我的订单', '待支付'],
        delivery: ['我的订单', '待发货'],
        receiving: ['我的订单', '待收货'],
        evaluate: ['我的订单', '待评价'],
        sign: ['我的订单', '已签收'],
        account: ['账号设置', '账号信息'],
        address: ['账号设置', '收货信息']
      },
      address: ''
    }
  },
  methods: {
    stretch (judge) {
      this.judge = judge
      emitter.emit('stretch', { aim: judge })
    }
  },
  watch: {
    $route: {
      handler (newValue, oldValue) {
        this.address = newValue.name
      },
      deep: true,
      immediate: true
    }
  }
}
</script>

<style scoped lang="less">
#brain {
  width: 100%;
  min-width: 1059px;
  height: 86px;
  display: flex;
  align-items: center;
  padding-left: 15px;
  border-bottom: 1px solid #ccc;
  background-color: #EEF4F9;
  .stretch {
    cursor: pointer;
    font-size: 20px;
    margin-right: 15px;
    &:hover {
      color: #409EFF;
    }
  }
}
</style>
