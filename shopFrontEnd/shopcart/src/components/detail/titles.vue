<template>
  <div class="detail_title">
    <div></div>
  </div>
</template>

<script>
export default {
  name: 'titles'
}
</script>

<style scoped lang="less">
.detail_title {
  width: 100%;
  height: 110px;
  overflow: hidden;
  position: relative;
  /*img {
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);
  }*/
  div {
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);
    background-image: url('https://w.wallhaven.cc/full/dp/wallhaven-dpjyvg.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    width: 100%;
    height: 100%;
  }
}
</style>
