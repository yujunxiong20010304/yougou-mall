<template>
  <el-space direction="vertical" alignment="flex-start">
    <el-skeleton style="width: 1190px;margin: 0 auto;" :loading="loading" animated :count="1">
      <template #template>
        <div class="commodity-display">
          <div style="width: 225px;height: 325px;margin: 0 6px 15px 7px;" v-for="i in 50">
            <el-skeleton-item variant="image" style="width: 222px; height: 215px" />
            <el-skeleton-item variant="h1" style="width: 100%;height: 34px;margin-top: 7px;" />
            <el-skeleton-item variant="h1" style="width: 100%;height: 47px;" />
          </div>
        </div>
      </template>
      <template #default>
        <div class="main">
          <div class="commodity-display">
            <div class="shop" v-for="item in shops" :key="item.id" @click="choice(item.id)">
              <img :src="item.goods_image" alt="">
              <span class="price"><i>特卖价</i><span>¥{{item.min_price}}.00</span></span>
              <span class="introduce">{{item.title}}</span>
            </div>
          </div>
          <el-pagination background layout="prev, pager, next" :page-count="total" @current-change="SwitchPages" :current-page="index" :hide-on-single-page="true"/>
        </div>
      </template>
    </el-skeleton>
  </el-space>
</template>

<script>

import emitter from '@/utils/event'

export default {
  name: 'CommodityDisplay',
  data () {
    return {
      total: 30,
      index: 1,
      shops: '',
      loading: true
    }
  },
  methods: {
    choice (id) {
      const newpage = this.$router.resolve({
        path: '/detail', // 跳转的页面路由
        query: { // 要传的参数
          id: id
        }
      })
      window.open(newpage.href, '_blank')
    },
    SwitchPages (index) {
      this.index = index
      // this.getSearchShop()
      this.$router.push({
        path: '/search',
        query: {
          search: this.$route.query.search,
          index: index,
          brand: this.$route.query.brand,
          rule: this.$route.query.rule,
          price: this.$route.query.price,
          sales: this.$route.query.sales,
          min_price: this.$route.query.min_price,
          max_price: this.$route.query.max_price
        }
      })
    },
    async getSearchShop () {
      this.loading = true
      const { data: res } = await this.$http.post('store/search/',
        {
          search: this.$route.query.search,
          index: this.$route.query.index,
          brand: this.$route.query.brand,
          aim: parseInt(this.$route.query.rule),
          price: parseInt(this.$route.query.price),
          sales: parseInt(this.$route.query.sales)
        }
      )
      if (res.code === 200) {
        emitter.emit('err', { aim: 1 })
        this.shops = res.data
        this.total = res.number
        this.loading = false
      } else {
        // 返回错误信息
        emitter.emit('err', { aim: 0 })
      }
    }
  },
  watch: {
    '$route.query.index': {
      handler (newVal, oldVal) {
        this.index = parseInt(newVal)
      },
      immediate: true
    },
    '$route.query': {
      handler (newVal, oldVal) {
        this.getSearchShop()
      }
    }
  },
  created () {
    this.getSearchShop()
  }
}
</script>

<style scoped lang="less">
.main {
  width: 1190px;
  margin: 0 auto;
}
.commodity-display {
  width: 1190px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  .shop {
    width: 225px;
    height: 325px;
    border: 1px solid #E7E7E7;
    cursor: pointer;
    border-radius: 5px;
    overflow: hidden;
    margin: 0 6px 15px 7px;
    &:hover {
      border: 1px solid #409EFF;
    }
    img {
      width: 222px;
      height: 215px;
    }
    .price {
      display: flex;
      align-items: center;
      padding-left: 7px;
      margin-top: 7px;
      i {
        font-style: normal;
        color: #fff;
        display: inline-block;
        background-image: linear-gradient(270deg,#e456ff 0,#ff31a3 100%);
        font-size: 12px;
        padding: 2px 7px;
        border-radius: 15px;
        margin-right: 5px;
      }
      span {
        color: #333;
        font-weight: 700;
        font-size: 23px;
      }
    }
    .introduce {
      margin-top: 11px;
      font-size: 13px;
      text-align: left;
      padding: 0 7px;
      overflow: hidden;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      text-overflow: ellipsis;
      height: 36px;
    }
  }
}
:deep(.el-pagination) {
  margin: 45px auto 25px;
  justify-content: center;
}
</style>
