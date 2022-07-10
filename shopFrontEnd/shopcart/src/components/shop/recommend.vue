<template>
  <div id="recommend">
    <img src="@/assets/backImage/recommend.png" alt="" />
    <ul id="nav">
      <li v-for="(item,index) in this.navigation" :key="index" @click="choices(index)" :class="[index === aim?'choice':'']">
        <span v-for="(item, index) in item" :key="index">{{item}}</span>
      </li>
    </ul>
    <!-- 内容 -->
    <div id="content">
      <exhibition v-for="item in msg" :key="item.id" :data="item" @click="goDetail(item.id)"></exhibition>
    </div>
  </div>
</template>

<script>
import exhibition from '@/components/shop/exhibition'
import emitter from '@/utils/event'
export default {
  name: 'recommend',
  components: {
    exhibition
  },
  props: ['msg'],
  data () {
    return {
      navigation: {
        0: ['精选', '猜你喜欢'],
        1: ['智能先锋', '大电器城'],
        2: ['居家优品', '品质生活'],
        3: ['超市百货', '百货生鲜'],
        4: ['时尚达人', '美妆穿搭'],
        5: ['优购国际', '进口好物'],
        6: ['热销商品', '全名口碑']
      },
      aim: '0'
    }
  },
  methods: {
    choices (index) {
      this.aim = index
      emitter.emit('recommend', { aim: this.aim })
    },
    goDetail (id) {
      const newpage = this.$router.resolve({
        path: '/detail', // 跳转的页面路由
        query: { // 要传的参数
          id: id
        }
      })
      window.open(newpage.href, '_blank')
    }
  }
}
</script>

<style scoped lang="less">
#recommend {
  width: 1155px;
  margin: 0 auto;
  img {
    width: 1155px;
  }
  #nav {
    display: flex;
    justify-content: space-around;
    margin: 0;
    padding: 0;
    .choice {
      span:last-child {
        color: #D1414D;
      }
      span:first-child {
        color: #fff;
        background-color: #E1251B;
        border-radius: 15px;
      }
    }
    li {
      background-color: white;
      width: 165px;
      height: 65px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      cursor: pointer;
      &:after {
        content: '';
        display: block;
        height: 35px;
        width: 1px;
        background-color: #E8E8E8;
        position: absolute;
        right: 0;
      }
      span:first-child {
        color: #666;
        font-size: 16px;
        font-weight: 700;
        width: 80px;
        height: 27px;
        padding: 0 5px;
        line-height: 27px;
      }
      span:last-child {
        color: #999;
        font-size: 14px;
      }
      &:hover span{
        color: #D1414D;
      }
    }
    li:last-child:after{
      display: none;
    }
  }
  #content{
    width: 1155px;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
  }
}
</style>
