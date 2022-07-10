<template>
<div class="similar-praise">
    <div class="guarantee-title">类似好评商品</div>
    <ul class="praises">
      <li v-for="(item,index) in shops" :key="item.id">
          <img :src="item.goods_image" :alt="index" />
          <span class="praise-introduce">
              {{item.title}}
          </span>
          <div class="praises-pic">
              <span class="pic">¥ {{item.min_price}}.00</span>
              <span><i class="iconfont">&#xe65d;</i>关注</span>
          </div>
          <div class="praises-tail"></div>
      </li>
    </ul>
</div>
</template>

<script>
export default {
  name: 'similar',
  data () {
    return {
      shops: ''
    }
  },
  methods: {
    async GetLookShop () {
      const { data: res } = await this.$http.post('store/goods/', { theme: '零食', number: 160, interval: 8 })
      if (res.code === 200) {
        this.shops = res.data
      }
    }
  },
  created () {
    this.GetLookShop()
  }
}
</script>

<style scoped lang="less">
.guarantee-title {
  margin-bottom: 15px;
  text-align: left;
  width: 968px;
  height: 20px;
  padding: 10px;
  box-sizing: content-box;
  background-color: #f7f7f7;
  border: 1px solid #eee;
  font: 700 14px "microsoft yahei";
  margin-top: 20px;
}
.praises {
  display: flex;
  flex-wrap: wrap;
  margin: 0;
  padding: 0;
  justify-content: space-between;
  li {
    margin: 10px 10px;
    border: 1px solid #f5f5f5;
    &:hover {
      box-shadow:0 15px 35px rgba(0,0,0,0.2),0 3px 10px rgba(0,0,0,0.2);
    }
  }
  img {
    width: 220px;
    height: 220px;
    margin-bottom: 5px;
  }
}
.praise-introduce {
  font-size: 12px;
  color: #666;
  width: 218px;
  height: 36px;
  padding: 0 9px;
  display: -webkit-box;
  -webkit-line-clamp: 2;  /*数字是几就显示几行*/
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-align: left;
}
.praises-pic {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: #666;
  padding: 0 5px;
}
.pic {
  color: #e4393c;
  font-size: 14px;
  font-weight: 700;
}
.praises-tail {
  width: 100%;
  height: 20px;
  background-color: #f7f7f7;
}
.ch-re {
  border: 2px solid red;
  box-sizing: border-box;
  padding: 0;
}
</style>
