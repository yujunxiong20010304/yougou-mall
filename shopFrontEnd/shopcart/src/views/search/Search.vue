<template>
  <all-header></all-header>
  <all-search></all-search>
  <error-prompt v-show="!judge"></error-prompt>
  <commodity-category v-show="judge"></commodity-category>
  <commodity-display v-show="judge"></commodity-display>
  <all-tail></all-tail>
  <el-backtop :bottom="100" :right="7">
    <img src="@/assets/backImage/rocket.png" alt="" style="height: 100%;width: 100%;"/>
  </el-backtop>
</template>

<script>
import CommodityCategory from '@/components/search/CommodityCategory'
import CommodityDisplay from '@/components/search/CommodityDisplay'
import ErrorPrompt from '@/components/search/ErrorPrompt'
import emitter from '@/utils/event'
export default {
  name: 'search',
  components: {
    'commodity-category': CommodityCategory,
    'commodity-display': CommodityDisplay,
    'error-prompt': ErrorPrompt
  },
  data () {
    return {
      judge: 1
    }
  },
  created () {
    emitter.on('err', (e) => {
      this.judge = e.aim
    })
  }
}
</script>

<style scoped lang="less">
:deep(.el-backtop) {
  box-shadow: none;
  &:hover {
    background-color: rgba(255, 255, 255, .1);
  }
}
</style>
