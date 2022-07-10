<template>
  <section id="heads">
    <div>优购</div>
    <ul>
      <li v-for="item in process">
        <span v-if="item">{{item[0]}}</span>
        <span v-if="item">{{item[1]}}</span>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'heads',
  data () {
    return {
      process: {
        0: [1, '拍下商品'],
        1: '',
        2: [2, '商品付款'],
        3: '',
        4: [3, '确认收货'],
        5: '',
        6: [4, '商品评价']
      }
    }
  }
}
</script>

<style scoped lang="less">
#heads {
  width: 990px;
  height: 89px;
  display: flex;
  overflow: hidden;
  align-items: center;
  justify-content: space-between;
  margin: 25px auto 0;
  div {
    width: 225px;
    font-size: 35px;
  }
  ul {
    display: flex;
    width: 55%;
    justify-content: space-between;
    margin: 0;
    padding: 0;
    li {
      &:nth-child(odd){
        width: 95px;
        height: 65px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;

      }
      &:nth-child(even){
        width: 129.5px;
        height: 1px;
        background: #c4c6cf;
        margin-top: 16px;
      }
      &:first-child{
        span {
          &:first-child {
            background-color: #FF0036;
            color: #fff;
            border: 0;
            font-weight: bold;
          }
        }
      }
      span {
        &:first-child{
          width: 32px;
          height: 32px;
          border-radius: 50%;
          display: block;
          text-align: center;
          line-height: 32px;
          color: #666;
          border: 1px solid #A0A2AD;
          cursor: pointer;
        }
        &:last-child {
          color: #333;
          font-size: 16px;
          font-weight: 700;
        }
      }
    }
  }
}
</style>
