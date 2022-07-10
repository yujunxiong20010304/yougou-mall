<template>
  <div>
    <all-header></all-header>
    <all-search></all-search>
    <mutual-evaluate></mutual-evaluate>
    <all-tail></all-tail>
  </div>
</template>

<script>
import mutualEvaluate from '@/components/evaluate/mutualEvaluate'
export default {
  name: 'Mutual',
  components: {
    'mutual-evaluate': mutualEvaluate
  }
}
</script>

<style scoped lang="less">

</style>
