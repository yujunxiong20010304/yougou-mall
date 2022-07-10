<template>
  <div id="user">
    <div class="layout">
      <div id="sidebar" :style="{ height: height + 'px' }">
         <el-menu
        :default-active="route_way"
        class="el-menu-vertical-demo"
        :collapse="isCollapse"
        :router="true"
        >
          <el-menu-item index="/user/yougou">
            <el-icon class="iconfont">&#xe6a4;</el-icon>
            <template #title>我的优购</template>
          </el-menu-item>
          <el-sub-menu index="1">
            <template #title>
              <el-icon class="iconfont">&#xe693;</el-icon>
              <span>我的订单</span>
            </template>
              <el-menu-item index="/user/shopcart">购物车</el-menu-item>
              <el-menu-item index="/user/payoff">待付款</el-menu-item>
              <el-menu-item index="/user/delivery">待发货</el-menu-item>
              <el-menu-item index="/user/receiving">待收货</el-menu-item>
              <el-menu-item index="/user/evaluate">待评价</el-menu-item>
              <el-menu-item index="/user/sign">已签收</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="2">
            <template #title>
              <el-icon class="iconfont">&#xe694;</el-icon>
              <span>账号设置</span>
            </template>
              <el-menu-item index="/user/account">账号信息</el-menu-item>
              <el-menu-item index="/user/address">收货信息</el-menu-item>
          </el-sub-menu>

          <el-sub-menu index="3">
            <template #title>
              <el-icon class="iconfont">&#xe697;</el-icon>
              <span>我的关注</span>
            </template>
              <el-menu-item index="3-1">关注店铺</el-menu-item>
              <el-menu-item index="3-2">关注商品</el-menu-item>
          </el-sub-menu>
        </el-menu>
      </div>
      <div class="content">
        <brain></brain>
        <div id="container" :style="{ height: height-86 + 'px' }" ref="container">
          <router-view ref="child" @childClick="childClick"></router-view>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import emitter from '@/utils/event'
import brain from '@/components/user/brain' // 头部导航
export default {
  name: 'test',
  components: {
    brain: brain
  },
  data () {
    return {
      isCollapse: true,
      height: '',
      route_way: ''
    }
  },
  methods: {
    childClick (e) {
      this.$refs.container.scrollTop = 0
    }
  },
  mounted () {
    emitter.on('stretch', (e) => {
      this.isCollapse = e.aim
    })
    // 设置窗口大小
    this.height = document.documentElement.clientHeight
    window.onresize = () => {
      return (() => {
        this.height = document.documentElement.clientHeight
      })()
    }
  },
  watch: {
    $route: { // $route可以用引号，也可以不用引号
      handler (to, from) {
        this.route_way = to.path
      },
      deep: true, // 深度监听
      immediate: true // 第一次初始化渲染就可以监听到
    }
  }
}
</script>

<style scoped lang="less">
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  height: 100%;
}
.el-menu--collapse {
  height: 100%;
}
.layout {
  display: flex;
  .content {
    display: flex;
    flex-direction: column;
    width: 100%;
    #container {
      width: 100%;
      min-width: 1059px;
      overflow: auto;
      padding: 10px;
    }
  }
}
</style>
