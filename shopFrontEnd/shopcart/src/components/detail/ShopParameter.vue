<template>
  <div class="parameter" v-if="details_args">
    <span>
        <i>{{details_args[0]}}</i>
    </span>
    <ul class="p-parameter-list" >
      <li v-for="(item, index) in details_args.slice(1)" :key="index">{{item}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ShopParameter',
  props: ['details_args']
}
</script>

<style scoped lang="less">
.parameter {
  font-size: 12px;
  color: #717171;
  border-bottom: 1px solid #EEEEEE;
  text-align: left;
  span {
    padding-left: 42px;
    padding-top: 20px;
    display: inline-block;
    width: 100%;
    i {
      font-style: normal;
    }
  }
}

.p-parameter-list {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  justify-content: flex-start;
  padding: 20px 0 15px 0;
  li {
    padding-left: 42px;
    margin-bottom: 5px;
    width: 200px;
    height: 18px;
    line-height: 18px;
    box-sizing: content-box;
    overflow: hidden;
    text-overflow:ellipsis;
    white-space: nowrap;
  }
}
</style>
