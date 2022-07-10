<template>
  <div id="image-parameter">
    <img :src="item" alt="" v-for="(item,index) in image_args" :key="index">
  </div>
</template>

<script>
export default {
  name: 'ImageParameter',
  props: ['image_args']
}
</script>

<style scoped lang="less">
#image-parameter {
  margin-top: 20px;
  img {
    width: 990px;
  }
}

</style>
